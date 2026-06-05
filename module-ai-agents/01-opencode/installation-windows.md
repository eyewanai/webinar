# Установка OpenCode на Windows

На Windows установка OpenCode имеет два рабочих сценария: прямой запуск в Windows и рекомендованный для учебных и рабочих задач вариант через WSL. Для начинающих специалистов удобнее объяснять оба, но сразу показывать, почему WSL обычно надежнее.

## Что понадобится

- Windows;
- терминал;
- Node.js;
- npm;
- доступ в интернет;
- при выборе WSL — установленный Windows Subsystem for Linux.

Официальные ссылки:

- [OpenCode Windows (WSL)](https://opencode.ai/docs/windows-wsl/)
- [OpenCode Intro](https://opencode.ai/docs/)
- [OpenCode Download](https://opencode.ai/download)
- [Node.js Downloads](https://nodejs.org/en/download)
- [Microsoft WSL documentation](https://learn.microsoft.com/windows/wsl/)

## Рекомендованный вариант: WSL

Официальная документация OpenCode рекомендует WSL как лучший опыт для Windows.

Почему это важно:

- Linux-окружение обычно лучше совместимо с терминальными агентами;
- меньше проблем с путями, правами и инструментами;
- проще повторять лабораторные задания.

### Шаг 1. Установите WSL

Следуйте официальному руководству Microsoft:

```bash
wsl --install
```

Если WSL уже установлен, проверьте дистрибутив:

```bash
wsl -l -v
```

### Шаг 2. Установите Node.js внутри WSL

Убедитесь, что `node` и `npm` доступны именно внутри Linux-окружения:

```bash
node -v
npm -v
```

### Шаг 3. Установите OpenCode

```bash
npm install -g opencode-ai
```

### Шаг 4. Проверьте запуск

```bash
opencode --help
opencode
```

## Прямой вариант в Windows

Если по внутренним причинам вы не можете использовать WSL, OpenCode также упоминает установку в Windows через менеджеры пакетов и npm.

### Через npm

```bash
npm install -g opencode-ai
```

### Через Chocolatey

```bash
choco install opencode
```

### Через Scoop

```bash
scoop install opencode
```

## Обновление

Для npm:

```bash
npm install -g opencode-ai
```

Для WSL-подхода обновляйте пакет внутри Linux-окружения, а не в обычном cmd.exe.

## Практические команды

```bash
wsl --install
wsl -l -v
node -v
npm -v
npm install -g opencode-ai
opencode --help
```

## TODO: screenshot

TODO: screenshot

## Что должно получиться

- WSL установлен и доступен, если вы выбрали рекомендованный сценарий;
- Node.js и npm работают;
- OpenCode запускается без ошибок;
- вы понимаете, где выполняется команда: в Windows или внутри WSL.

## Проверка результата

- выполните `wsl -l -v`;
- проверьте `node -v` и `npm -v`;
- выполните `opencode --help`;
- если есть проблемы, сравните вашу схему с официальной страницей OpenCode для Windows (WSL).

