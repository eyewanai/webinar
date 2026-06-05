# Полезные ссылки

Этот список нужен как опорный справочник. В учебной работе важно опираться на официальные источники, а не на случайные пересказы или устаревшие блоги.

## Ссылки

- [OpenCode documentation](https://opencode.ai/docs/)
- [OpenCode config](https://opencode.ai/docs/config/)
- [OpenCode models](https://opencode.ai/docs/models/)
- [OpenCode MCP servers](https://opencode.ai/docs/mcp-servers/)
- [MCP docs](https://modelcontextprotocol.io/docs/learn)
- [Playwright MCP getting started](https://playwright.dev/docs/getting-started-mcp)
- [Apple Security Releases](https://support.apple.com/en-us/100100)
- [Microsoft Security Update Guide](https://msrc.microsoft.com/update-guide/)
- [CVE Program](https://www.cve.org/)
- [CVE Program overview](https://www.cve.org/about/overview)
- [NVD](https://nvd.nist.gov/)
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

## Зачем этот список нужен

- чтобы студент быстро открывал первоисточник;
- чтобы преподаватель мог ссылаться на один набор официальных страниц;
- чтобы исключить зависимость от неофициальных пересказов;
- чтобы следующий проект можно было собрать по той же схеме.

## Практические команды

Проверка доступности официальных страниц:

```bash
curl -I https://opencode.ai/docs/
curl -I https://playwright.dev/docs/getting-started-mcp
curl -I https://support.apple.com/en-us/100100
curl -I https://msrc.microsoft.com/update-guide/
```

## TODO: screenshot

TODO: screenshot

## Что должно получиться

- у вас есть единый список официальных источников;
- вы можете быстро открыть нужную документацию;
- у студентов есть проверяемая база ссылок;
- список пригоден для публикации вместе с курсом.

## Проверка результата

- убедитесь, что каждая ссылка ведет на официальный сайт;
- проверьте доступность ключевых страниц;
- убедитесь, что нет неофициальных альтернатив вместо первоисточников;
- подтвердите, что список покрывает OpenCode, MCP, Playwright, Apple, Microsoft, MITRE, NVD и CISA.
