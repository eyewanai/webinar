# Модуль: AI Agents, OpenCode и MCP для Threat Intelligence

Этот учебный модуль объясняет, как устроены AI-агенты в терминале, зачем им нужны инструменты, как подключается MCP, и как применять это в задачах Threat Intelligence и SOC. Материал написан для людей, которые раньше не работали с MCP, браузерной автоматизацией и агентными пайплайнами.

## Что вы изучите

- что такое OpenCode и чем он отличается от обычного ChatGPT;
- зачем агенту нужны инструменты и почему без них он быстро упирается в ограничения;
- что такое MCP и как подключать локальные и удаленные серверы;
- как установить и настроить OpenCode на macOS, Linux и Windows;
- как использовать Playwright MCP для автоматизации браузера;
- как собрать практический пайплайн для извлечения CVE из Apple Security Updates;
- как оформить домашнее задание на основе Microsoft MSRC;
- какие ошибки встречаются чаще всего и как их диагностировать.

## Для кого этот модуль

- начинающие специалисты Threat Intelligence;
- специалисты SOC;
- аналитики информационной безопасности;
- инженеры автоматизации;
- пользователи, которые впервые сталкиваются с MCP и агентами;
- преподаватели и менторы, которым нужен готовый учебный материал.

## Требования

- базовое понимание того, что такое CVE;
- умение работать с терминалом;
- установленный Node.js;
- доступ к одному или нескольким провайдерам моделей;
- современный браузер для практики с Playwright MCP;
- желание читать логи и проверять результат по шагам.

## Ожидаемый результат

После прохождения модуля студент сможет:

- установить OpenCode и базово его настроить;
- подключить MCP-серверы;
- понимать, как агент выбирает инструменты;
- запускать браузерную автоматизацию через Playwright MCP;
- извлекать уязвимости из публичных бюллетеней;
- сохранять результат в JSON;
- обогащать данные через MITRE/CVE и использовать это для дальнейшего анализа.

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
- [05-additional-materials/common-errors.md](./05-additional-materials/common-errors.md)
- [05-additional-materials/ideas-for-further-study.md](./05-additional-materials/ideas-for-further-study.md)

## Как пользоваться модулем

1. Начните с раздела про OpenCode, чтобы понять базовую модель работы агента.
2. Затем перейдите к MCP и Playwright MCP, чтобы увидеть, как агент получает инструменты.
3. После этого разберите практический кейс по Apple.
4. Завершите модуль домашним заданием по Microsoft MSRC.
5. Используйте дополнительные материалы как справочник для следующих проектов.

## TODO: screenshot

TODO: screenshot

## Что должно получиться

- у вас есть полный набор Markdown-файлов для публикации студентам;
- структура модулей совпадает с учебным планом;
- каждый файл содержит объяснение, команды, результат и проверку;
- ссылки ведут на официальную документацию.

## Проверка результата

- откройте этот файл и проверьте, что ссылки ведут в нужные разделы;
- проверьте, что в каталоге `module-ai-agents/` присутствуют все файлы из структуры;
- убедитесь, что каждый документ написан на русском языке и содержит практические примеры;
- проверьте, что в каждом файле присутствует блок `TODO: screenshot`.

