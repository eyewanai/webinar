# Идеи для дальнейшего изучения

После базового модуля попробуйте подключить новый официальный источник к тому же пайплайну.

## Следующие источники

- Cisco Security Advisories;
- Fortinet PSIRT;
- Palo Alto advisories;
- Android Security Bulletins;
- Mozilla Advisories;
- GitHub Security Advisories.

## Зачем это нужно

У этих источников похожая логика: меняется входной сайт, но общий пайплайн сохраняется.

Схема обычно такая:

1. Открыть официальный advisory.
2. Найти записи за нужный период.
3. Извлечь CVE.
4. Нормализовать структуру.
5. Обогатить через MITRE, NVD или CISA KEV.
6. Сохранить JSON.

## Как подключить новый источник к тому же пайплайну

### Cisco Security Advisories

- подставьте официальный Cisco advisory page;
- настройте фильтр по году и месяцу;
- извлекайте CVE из текста;
- сохраняйте структуру в том же JSON-формате.

### Fortinet PSIRT

- используйте официальный PSIRT feed или advisory page;
- адаптируйте регулярное выражение и навигацию;
- проверьте, есть ли отдельные страницы под каждую запись.

### Palo Alto advisories

- найдите официальный advisory center;
- сопоставьте названия продуктов;
- добавьте дедупликацию.

### Android Security Bulletins

- используйте официальные monthly bulletins;
- извлекайте CVE и компоненты Android;
- сохраняйте данные в той же структуре.

### Mozilla Advisories

- используйте официальный security advisories page;
- проверьте типы релизов и продуктовые ветки;
- нормализуйте выходные данные.

### GitHub Security Advisories

- используйте официальный advisory portal;
- сопоставляйте пакеты и версии;
- не путайте advisory и CVE.

## Практические команды

Проверка базовой идеи повторяемости пайплайна:

```bash
cat module-ai-agents/03-practice-apple/walkthrough.md
cat module-ai-agents/04-homework-microsoft/prompt.md
```

Ожидаемый результат: вы видите два примера одного подхода на разных источниках.
