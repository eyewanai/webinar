# Подключение собственного MCP-сервера в OpenCode

Цель: подключить собственный TI-сервер к OpenCode вместе с Playwright MCP.

## Пример конфигурации

Этот конфиг включает два сервера: Playwright для браузера и `ti-tools` для IOC:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "playwright": {
      "type": "local",
      "command": [
        "npx",
        "-y",
        "@playwright/mcp@latest",
        "--browser=chromium",
        "--headless"
      ],
      "enabled": true
    },
    "ti-tools": {
      "type": "remote",
      "url": "http://127.0.0.1:8000/mcp",
      "enabled": true
    }
  }
}
```

## Почему здесь используется remote

FastMCP слушает `localhost` по HTTP, поэтому OpenCode подключается к нему как к remote MCP-серверу.

## Почему ключ лучше держать в окружении

В примере это допустимо, но для нормальной работы лучше хранить ключ в переменной окружения:

```bash
export RST_THREAT_API_KEY="your-api-key-here"
opencode
```

Ожидаемый результат: OpenCode запускается в сессии, где доступен `RST_THREAT_API_KEY`.

Тогда ключ не попадает в JSON.

## Как проверить, что сервер виден

После запуска OpenCode проверьте, что доступны оба MCP-сервера:

- `playwright`;
- `ti-tools`.

Если `ti-tools` не виден, сначала проверьте:

```bash
curl -i http://127.0.0.1:8000/mcp
```

Ожидаемый результат: локальный сервер отвечает по HTTP.

Затем проверьте ключ и перезапустите OpenCode.

## Практические команды

Проверить путь к Python:

```bash
which python
```

Ожидаемый результат: путь указывает на Python из виртуального окружения, если оно используется.

Проверить ключ:

```bash
echo "$RST_THREAT_API_KEY"
```

Ожидаемый результат: терминал выводит ключ или пустую строку, если переменная не задана.

Запустить OpenCode:

```bash
opencode
```

Ожидаемый результат: OpenCode запускается и видит настроенные MCP-серверы после перезапуска.

## Проверка результата

- Playwright MCP подключен;
- собственный TI MCP подключен через `http://127.0.0.1:8000/mcp`;
- ключ задан в окружении, а не в JSON;
- OpenCode видит `ti-tools` как remote MCP.
