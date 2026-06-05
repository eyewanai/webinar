# Модуль: AI Agents, OpenCode и MCP для Threat Intelligence

Этот модуль объясняет, как устроены AI-агенты в терминале, зачем им нужны инструменты, как подключается MCP и как применять это в задачах Threat Intelligence и SOC. Материал написан для тех, кто раньше не работал с MCP, браузерной автоматизацией и агентными пайплайнами.

## Что вы изучите

- что такое OpenCode и чем он отличается от обычного ChatGPT;
- зачем агенту нужны инструменты и почему без них он быстро упирается в ограничения;
- что такое MCP и как подключать локальные и удаленные серверы;
- как установить и настроить OpenCode на macOS, Linux и Windows;
- как использовать Playwright MCP для автоматизации браузера;
- как собрать практический пайплайн для извлечения CVE из Apple Security Updates;
- как оформить домашнее задание на основе Microsoft MSRC;
- какие ошибки встречаются чаще всего и как их диагностировать.

## Требования

- базовое понимание того, что такое CVE;
- умение работать с терминалом;
- установленный Node.js;
- доступ к одному или нескольким провайдерам моделей;
- современный браузер для практики с Playwright MCP;
- желание читать логи и проверять результат по шагам.

## Навигация по разделам

- [01-opencode/README.md](./01-opencode/README.md)
- [01-opencode/installation-macos.md](./01-opencode/installation-macos.md)
- [01-opencode/installation-linux.md](./01-opencode/installation-linux.md)
- [01-opencode/installation-windows.md](./01-opencode/installation-windows.md)
- [01-opencode/configuration.md](./01-opencode/configuration.md)
- [01-opencode/models.md](./01-opencode/models.md)
- [01-opencode/mcp-overview.md](./01-opencode/mcp-overview.md)
- [02-playwright-mcp/README.md](./02-playwright-mcp/README.md)
- [02-playwright-mcp/installation.md](./02-playwright-mcp/installation.md)
- [02-playwright-mcp/configuration.md](./02-playwright-mcp/configuration.md)
- [02-playwright-mcp/troubleshooting.md](./02-playwright-mcp/troubleshooting.md)
- [03-practice-apple/README.md](./03-practice-apple/README.md)
- [03-practice-apple/task.md](./03-practice-apple/task.md)
- [03-practice-apple/prompt.md](./03-practice-apple/prompt.md)
- [03-practice-apple/walkthrough.md](./03-practice-apple/walkthrough.md)
- [04-homework-microsoft/README.md](./04-homework-microsoft/README.md)
- [04-homework-microsoft/task.md](./04-homework-microsoft/task.md)
- [04-homework-microsoft/prompt.md](./04-homework-microsoft/prompt.md)
- [05-additional-materials/useful-links.md](./05-additional-materials/useful-links.md)
- [05-additional-materials/skills.md](./05-additional-materials/skills.md)
- [FAQ.md](./FAQ.md)
- [05-additional-materials/ideas-for-further-study.md](./05-additional-materials/ideas-for-further-study.md)
- [06. Создаём собственный MCP-сервер для Threat Intelligence](./06-custom-ti-mcp/README.md)

## Как пользоваться модулем

1. Начните с раздела про OpenCode, чтобы понять базовую модель работы агента.
2. Затем перейдите к MCP и Playwright MCP, чтобы увидеть, как агент получает инструменты.
3. После этого разберите практический кейс по Apple.
4. Завершите модуль домашним заданием по Microsoft MSRC.
5. Используйте дополнительные материалы как справочник для следующих проектов.
