# Ядро агента (C)

Ядро собирается в динамическую библиотеку: `sentry_core.dll` в Windows, `libsentry_core.dylib` в macOS,
`libsentry_core.so` в Linux. Первая функция появляется на паре 2.

| Файл | Что в нём |
|---|---|
| core.h | структура и объявление функции, шаг 5 |
| core_info.c | функция core_get_info, шаг 6 |
| show_info.c | программа проверки, шаг 7 |
