# Реализация MCP-сервера

Ниже полный код MCP-сервера для TI-задач. На первом проходе не нужно разбирать каждую строку. Достаточно понять роли частей:

1. Функция принимает данные и возвращает результат.
2. `@mcp.tool` делает функцию инструментом агента.
3. Агент вызывает инструмент, когда это нужно по задаче.

Перед чтением кода полезно держать в голове цепочку: текст статьи -> IOC -> нормализация -> enrichment -> JSON.

Enrichment, или обогащение, — это запрос к внешнему источнику за дополнительными сведениями об IOC. Defanged IOC — безопасная запись индикатора, например `example[.]com`.

## Файл `server.py`

```python
import json
import os
import re
from functools import lru_cache

import requests
from fastmcp import FastMCP


mcp = FastMCP("TI MCP Server")

RST_THREAT_API_URL = "https://api.cyberthreattech.ru/v1/ioc"


def normalize_ioc(ioc: str) -> str:
    """Normalize IOC text by stripping whitespace and converting [.] to ..

    Use this helper when an IOC arrives in defanged form and you need a stable
    value for lookup or enrichment.
    """
    return ioc.strip().replace("[.]", ".")


@mcp.tool
def extract_iocs_from_text(text: str) -> dict:
    """Extract defanged domains and IPv4 addresses from plain text.

    Pass raw article text to this tool when you need a deduplicated IOC list.
    The tool returns defanged domains, defanged IPv4 addresses, and the total
    number of unique IOC values found.
    """
    domain_regex = r"\b[a-zA-Z0-9.-]+\[\.\][a-zA-Z]{2,10}\b"
    ipv4_regex = r"\b(?:\d{1,3}\.){3}\d{1,3}\b|\b(?:\d{1,3}\[\.\]){3}\d{1,3}\b"

    domain_matches = re.findall(domain_regex, text)
    ipv4_matches = re.findall(ipv4_regex, text)

    domains = sorted(set(match.strip() for match in domain_matches))
    ipv4 = sorted(set(match.strip() for match in ipv4_matches))

    return {
        "domains": domains,
        "ipv4": ipv4,
        "total": len(domains) + len(ipv4),
    }


@lru_cache(maxsize=1024)
def _lookup_ioc_cached(normalized_ioc: str) -> dict:

    rst_threat_apikey = os.getenv("RST_THREAT_API_KEY")
    if not rst_threat_apikey:
        raise RuntimeError("RST_THREAT_API_KEY is not set")

    headers = {
        "accept": "application/json",
        "x-api-key": rst_threat_apikey,
    }
    params = {
        "value": normalized_ioc,
    }

    response = requests.get(RST_THREAT_API_URL, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


@mcp.tool
def lookup_ioc(ioc: str) -> dict:
    """Look up one IOC in the external enrichment API.

    Use this tool for a single IOC value, usually after normalization.
    The tool returns the raw API response or a structured error object if the
    request fails.
    """
    normalized_ioc = normalize_ioc(ioc)

    try:
        data = _lookup_ioc_cached(normalized_ioc)
        return data
    except Exception as exc:
        return {
            "ioc": ioc,
            "normalized_ioc": normalized_ioc,
            "error": str(exc),
        }


def _extract_description_fields(description: str | None) -> tuple[str | None, str | None]:
    """Try to pull tag and related threat information from a free-form description."""
    if not description:
        return None, None

    tag = None
    related_threat = None

    tag_match = re.search(r"(?i)\btag\s*[:=]\s*([A-Za-z0-9._-]+)", description)
    if tag_match:
        tag = tag_match.group(1).strip()

    threat_match = re.search(r"(?i)\b(?:threat|group|campaign|actor)\s*[:=]\s*([A-Za-z0-9._ -]+)", description)
    if threat_match:
        related_threat = threat_match.group(1).strip()

    return tag, related_threat


@mcp.tool
def enrich_ioc(ioc: str) -> dict:
    """Enrich a single IOC and return normalized metadata.

    Pass one IOC string, usually in defanged form. The tool normalizes it,
    calls the external API, and returns a compact record with useful fields for
    downstream analysis.
    """
    normalized_ioc = normalize_ioc(ioc)
    raw = lookup_ioc(ioc)

    if "error" in raw:
        return {
            "ioc": ioc,
            "normalized_ioc": normalized_ioc,
            "ioc_type": None,
            "tag": None,
            "related_threat": None,
            "report_source": None,
            "description": None,
            "raw": raw,
        }

    ioc_type = raw.get("ioc_type")
    description = raw.get("description")
    report_source = None

    src = raw.get("src")
    if isinstance(src, dict):
        report_source = src.get("report")

    tag, related_threat = _extract_description_fields(description if isinstance(description, str) else None)

    return {
        "ioc": ioc,
        "normalized_ioc": normalized_ioc,
        "ioc_type": ioc_type,
        "tag": tag,
        "related_threat": related_threat,
        "report_source": report_source,
        "description": description if isinstance(description, str) else None,
        "raw": raw,
    }


@mcp.tool
def enrich_iocs(iocs: list[str]) -> list[dict]:
    """Enrich a list of IOC values one by one.

    Use this tool when you already have a list of defanged IOCs and want a
    normalized enrichment record for each item.
    """
    results: list[dict] = []
    for ioc in iocs:
        results.append(enrich_ioc(ioc))
    return results


@mcp.tool
def save_iocs_to_json(filename: str, data: list[dict]) -> dict:
    """Save enrichment results to a JSON file.

    Pass the filename you want and a list of IOC records. The tool writes the
    file with readable formatting and returns a short summary for the agent.
    """
    with open(filename, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)

    return {
        "filename": filename,
        "records": len(data),
    }


if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)
```

## Как читать этот код

- верхняя часть подключает библиотеки и создает объект `FastMCP`;
- `extract_iocs_from_text()` ищет IOC в тексте;
- `lookup_ioc()` обращается к API;
- `enrich_ioc()` собирает удобную структуру;
- `enrich_iocs()` обрабатывает список;
- `save_iocs_to_json()` пишет JSON-файл;
- `mcp.run(...)` запускает сервер на `localhost:8000`.

## Практические команды

Проверить синтаксис Python-файла:

```bash
python3 -m py_compile server.py
```

Ожидаемый результат: команда завершается без вывода. Если есть ошибка синтаксиса, Python покажет строку с проблемой.

Запустить сервер:

```bash
python3 server.py
```

Ожидаемый результат: сервер запускается и остается работать в терминале. После этого его можно подключать из OpenCode.

## Проверка результата

- `normalize_ioc()` убирает пробелы и превращает `[.]` в `.`;
- `extract_iocs_from_text()` возвращает домены, IPv4 и total;
- `lookup_ioc()` возвращает raw-ответ или ошибку;
- `enrich_ioc()` не ломается на пустом `description`;
- `save_iocs_to_json()` пишет JSON в читаемом виде.
