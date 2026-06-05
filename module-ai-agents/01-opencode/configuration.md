# Конфигурация OpenCode

OpenCode хранит настройки в JSON-файле. Конфиг фиксирует модель, провайдера, инструменты и MCP-серверы.

## Где лежит конфиг

Пути к глобальному конфигу:

### macOS

```text
~/.config/opencode/opencode.json
```

### Linux

```text
~/.config/opencode/opencode.json
```

### Windows

```text
%USERPROFILE%\.config\opencode\opencode.json
```

Источник:

- [OpenCode Config](https://opencode.ai/docs/config/)

## Зачем нужен конфиг

Конфиг нужен, чтобы один раз задать:

- модель;
- провайдера;
- инструменты;
- MCP-серверы;
- права;
- подсказки и инструкции для агента.

Без конфига настройки приходится повторять вручную при каждом похожем запуске.

## Базовый пример

Этот пример показывает минимальный конфиг: схема, модель и автообновление.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-20250514",
  "autoupdate": true
}
```

## Пример с провайдером и MCP

Этот пример показывает, как брать API-ключ из переменной окружения и подключить Playwright MCP.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "openai/gpt-5",
  "provider": {
    "openai": {
      "options": {
        "apiKey": "{env:OPENAI_API_KEY}"
      }
    }
  },
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

## Пример с отключением лишних инструментов

Для повторяемых стендов лучше ограничить набор доступных инструментов:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "tools": {
    "write": false,
    "bash": false
  }
}
```

Это не «ломает» агента, а делает его поведение более предсказуемым в заданном сценарии.

## Как проверить конфиг

Проверяйте конфиг тремя способами:

1. Откройте файл в редакторе.
2. Проверьте синтаксис JSON.
3. Запустите OpenCode и убедитесь, что он подхватывает параметры.

## Практические команды

Проверьте, что OpenCode видит глобальный конфиг:

```bash
cat ~/.config/opencode/opencode.json
```

Ожидаемый результат: терминал выводит JSON-конфиг или сообщает, что файл отсутствует.

Проверьте, что OpenCode установлен и запускается:

```bash
opencode --help
```

Ожидаемый результат: OpenCode выводит справку.

Откройте список моделей, чтобы убедиться, что конфиг не мешает запуску клиента:

```bash
opencode /models
```

Ожидаемый результат: OpenCode показывает доступные модели.

На Windows:

```powershell
type %USERPROFILE%\.config\opencode\opencode.json
```

Ожидаемый результат: PowerShell выводит JSON-конфиг или сообщает, что файл отсутствует.
