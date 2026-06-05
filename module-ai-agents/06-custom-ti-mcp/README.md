# Собственный MCP-сервер для Threat Intelligence

Цель раздела: собрать небольшой MCP-сервер, который даст агенту TI-инструменты для IOC.

FastMCP — Python-библиотека, которая превращает обычные функции в инструменты MCP без ручной работы с протоколом.

Агент сможет:

- извлекать IOC из текста;
- нормализовать IOC;
- обогащать IOC через внешний API;
- сохранять результат в JSON.

## Что в разделе

- FastMCP;
- проект на Python;
- переменные окружения для API-ключа;
- инструменты для IOC;
- подключение Playwright и собственного TI-сервера в OpenCode;
- практика и troubleshooting.

## Как работает практика

Пайплайн выглядит так:

```text
OpenCode Agent
    ↓
Playwright MCP
    ↓
Открывает статью в браузере
    ↓
Получает текст страницы
    ↓
Custom TI MCP
    ↓
extract_iocs_from_text()
    ↓
lookup_ioc()
    ↓
save_json()
    ↓
ioc.json
```

Порядок работы простой:

1. Playwright открывает статью.
2. TI MCP извлекает и обогащает IOC.
3. Агент сохраняет `ioc.json`.

## Для кого этот раздел

Нужно уметь запускать OpenCode, подключать MCP-серверы и понимать, что такое IOC.

## Практические команды

Проверить, что Python доступен:

```bash
python3 --version
```

Ожидаемый результат: терминал выводит версию Python.

Проверить окружение:

```bash
pwd
ls
```

Ожидаемый результат: вы видите текущий каталог и список файлов проекта.

Проверить переменную окружения:

```bash
echo "$RST_THREAT_API_KEY"
```

Ожидаемый результат: терминал выводит API-ключ или пустую строку, если ключ еще не задан.

## Связанные файлы

- [fastmcp-overview.md](./fastmcp-overview.md)
- [project-setup.md](./project-setup.md)
- [server-implementation.md](./server-implementation.md)
- [opencode-configuration.md](./opencode-configuration.md)
- [practice-ioc-enrichment.md](./practice-ioc-enrichment.md)
- [prompt.md](./prompt.md)
- [troubleshooting.md](./troubleshooting.md)

## Критерий готовности

- Python доступен из терминала;
- OpenCode уже запускается;
- Playwright MCP подключен;
- вы знаете, где будет храниться API-ключ.
