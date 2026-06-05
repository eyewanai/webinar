# Конфигурация Playwright MCP

Цель файла: показать, как Playwright MCP подключается к OpenCode. Сервер может запускаться отдельно, но агент увидит его только после настройки клиента.

Ссылки:

- [Playwright MCP getting started](https://playwright.dev/docs/getting-started-mcp)

## Базовый пример конфигурации

Добавьте этот блок в конфиг OpenCode, чтобы клиент запускал Playwright MCP локально:

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
    }
  }
}
```

## Как читать этот конфиг

- `"$schema"` помогает редактору валидировать JSON.
- `mcp` — секция со всеми MCP-серверами.
- `playwright` — имя сервера внутри OpenCode.
- `type: "local"` означает локальный запуск процесса.
- `command` — команда, которая поднимает сервер.
- `enabled: true` включает сервер.

## Что можно менять

В зависимости от задачи можно менять:

- браузер;
- headless-режим;
- путь к конфигу сервера;
- транспорт, если сценарий это требует;
- список разрешенных инструментов в клиенте.

Пример изменения браузера:

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
        "--browser=firefox",
        "--headless"
      ],
      "enabled": true
    }
  }
}
```

## Зачем этот блок

Конфиг определяет:

- какие инструменты видит агент;
- как они стартуют;
- с какими параметрами они работают;
- почему одна и та же задача может вести себя по-разному на разных машинах.

## Практические команды

Проверить конфиг:

```bash
cat ~/.config/opencode/opencode.json
```

Ожидаемый результат: терминал выводит конфиг, где есть сервер `playwright`.

Проверить синтаксис через редактор или валидатор JSON:

```bash
node -e 'JSON.parse(require("fs").readFileSync(process.argv[1], "utf8")); console.log("ok")' ~/.config/opencode/opencode.json
```

Ожидаемый результат: команда выводит `ok`. Если есть ошибка, исправьте JSON перед запуском OpenCode.
