# Установка OpenCode на Windows

Цель: установить OpenCode на Windows. Рекомендуемый путь для курса — WSL, потому что он ближе к Linux-окружению практик.

## Что понадобится

- Windows;
- терминал;
- Node.js;
- npm;
- доступ в интернет;
- при выборе WSL — установленный Windows Subsystem for Linux.

Ссылки:

- [OpenCode Windows (WSL)](https://opencode.ai/docs/windows-wsl/)
- [OpenCode Intro](https://opencode.ai/docs/)
- [OpenCode Download](https://opencode.ai/download)
- [Node.js Downloads](https://nodejs.org/en/download)
- [Microsoft WSL documentation](https://learn.microsoft.com/windows/wsl/)

## Рекомендованный вариант: WSL

В документации OpenCode для Windows WSL рекомендуют как основной сценарий.

Почему выбирают WSL:

- Linux-окружение лучше совместимо с терминальными агентами;
- меньше проблем с путями, правами и инструментами;
- проще повторять лабораторные задания.

### Шаг 1. Установите WSL

Следуйте официальному руководству Microsoft:

```bash
wsl --install
```

Ожидаемый результат: Windows устанавливает WSL и предлагает перезагрузку, если она нужна.

Если WSL уже установлен, проверьте дистрибутив:

```bash
wsl -l -v
```

Ожидаемый результат: вы видите установленный Linux-дистрибутив и его состояние.

### Шаг 2. Установите Node.js внутри WSL

Убедитесь, что `node` и `npm` доступны именно внутри Linux-окружения:

```bash
node -v
npm -v
```

Ожидаемый результат: терминал WSL выводит версии Node.js и npm.

### Шаг 3. Установите OpenCode

Эта команда устанавливает OpenCode внутри WSL через npm:

```bash
npm install -g opencode-ai
```

Ожидаемый результат: npm завершает установку без ошибок.

### Шаг 4. Проверьте запуск

Первая команда проверяет справку, вторая запускает клиент:

```bash
opencode --help
opencode
```

Ожидаемый результат: `opencode --help` выводит справку, а `opencode` открывает интерактивный режим.

## Прямой вариант в Windows

Если WSL вам не подходит, OpenCode можно поставить прямо в Windows через npm или менеджеры пакетов.

### Через npm

Команда ставит OpenCode глобально через npm в Windows:

```bash
npm install -g opencode-ai
```

Ожидаемый результат: npm устанавливает пакет без ошибок.

### Через Chocolatey

Команда ставит OpenCode через Chocolatey:

```bash
choco install opencode
```

Ожидаемый результат: Chocolatey устанавливает пакет без ошибок.

### Через Scoop

Команда ставит OpenCode через Scoop:

```bash
scoop install opencode
```

Ожидаемый результат: Scoop устанавливает пакет без ошибок.

## Обновление

Для npm:

```bash
npm install -g opencode-ai
```

Ожидаемый результат: npm обновляет пакет или сообщает, что актуальная версия уже установлена.

Для WSL-подхода обновляйте пакет внутри Linux-окружения, а не в обычном `cmd.exe`.

## Критерий завершения

Установка завершена, если внутри выбранного окружения `node -v`, `npm -v` и `opencode --help` выводят результат без ошибок.
