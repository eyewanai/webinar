# Конфигурация OpenCode

OpenCode хранит настройки в JSON-файле. Для учебного процесса это удобно: конфиг можно проверить, повторить и версионировать отдельно от поведения агента.

## Где лежит конфиг

Официальные пути для глобальной конфигурации:

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

Официальный источник:

- [OpenCode Config](https://opencode.ai/docs/config/)

## Зачем нужен конфиг

Конфиг нужен, чтобы централизованно настроить:

- модель;
- провайдера;
- инструменты;
- MCP-серверы;
- права;
- подсказки и инструкции для агента.

Без конфига каждый запуск превращается в ручную настройку. Для учебной группы это почти всегда плохой вариант.

## Базовый пример

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-20250514",
  "autoupdate": true
}
```

## Пример с провайдером и MCP

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

Для учебных стендов полезно ограничивать набор доступных инструментов:

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

```bash
cat ~/.config/opencode/opencode.json
opencode --help
opencode /models
```

На Windows:

```powershell
type %USERPROFILE%\.config\opencode\opencode.json
```

## TODO: screenshot

TODO: screenshot

## Что должно получиться

- вы знаете точный путь к конфигу на своей платформе;
- вы понимаете, какие параметры настраиваются в `opencode.json`;
- вы можете проверить базовую конфигурацию перед запуском практики.

## Проверка результата

- откройте конфиг по пути вашей ОС;
- убедитесь, что JSON валиден;
- проверьте, что `"$schema"` указывает на официальный schema URL;
- запустите OpenCode и убедитесь, что он использует ваш конфиг.

