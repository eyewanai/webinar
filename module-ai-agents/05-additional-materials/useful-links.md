# Полезные ссылки

Список официальных источников для курса и самостоятельной проверки.

## Ссылки

- [OpenCode documentation](https://opencode.ai/docs/)
- [OpenCode config](https://opencode.ai/docs/config/)
- [OpenCode models](https://opencode.ai/docs/models/)
- [OpenCode MCP servers](https://opencode.ai/docs/mcp-servers/)
- [OpenCode skills](https://opencode.ai/docs/ru/skills/)
- [MCP docs](https://modelcontextprotocol.io/docs/learn)
- [Playwright MCP getting started](https://playwright.dev/docs/getting-started-mcp)
- [Apple Security Releases](https://support.apple.com/en-us/100100)
- [Microsoft Security Update Guide](https://msrc.microsoft.com/update-guide/)
- [CVE Program](https://www.cve.org/)
- [CVE Program overview](https://www.cve.org/about/overview)
- [NVD](https://nvd.nist.gov/)
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

## Зачем этот список нужен

- чтобы можно было быстро открыть первоисточник;
- чтобы можно было ссылаться на один набор официальных страниц;
- чтобы исключить зависимость от неофициальных пересказов;
- чтобы следующий проект можно было собрать по той же схеме.

## Практические команды

Проверка доступности официальных страниц:

```bash
curl -I https://opencode.ai/docs/
curl -I https://opencode.ai/docs/ru/skills/
curl -I https://playwright.dev/docs/getting-started-mcp
curl -I https://support.apple.com/en-us/100100
curl -I https://msrc.microsoft.com/update-guide/
```

Ожидаемый результат: каждая команда возвращает HTTP-заголовки. Если источник недоступен, проверьте сеть или повторите позже.
