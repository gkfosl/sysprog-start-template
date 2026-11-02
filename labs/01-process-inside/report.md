# ЛР 1. Процесс изнутри

Система:
ProductName:		macOS
ProductVersion:		27.0.1
BuildVersion:		26A434 
компилятор: Apple clang version 21.0.0 (clang-2100.0.123.102) (первая строка вывода версии)

## Программа на C
Программа напечатала PID agent v0, pid=26264, монитор показал PID 26264.
Память процесса в мониторе: физическая 784 КБ, виртуальная 466,14 ГБ, совместная 720 КБ, собственная 32 КБ. Процессорное время: 0,0.
Пока программа ждёт Enter, процессорное время не растёт, потому что процесс заблокирован в getchar() и ОС не выделяет ему процессор, пока не придёт ввод.
Дескрипторов у процесса:
/dev/ttys024
/dev/ttys024
/dev/ttys024. 
Ввод и вывод ведут в терминал.
Системные библиотеки в процессе: 
/usr/lib/system/libcache.dylib
/usr/lib/system/libcommonCrypto.dylib
/usr/lib/system/libcompiler_rt.dylib
/usr/lib/system/libcopyfile.dylib
/usr/lib/system/libcorecrypto.dylib
/usr/lib/system/libdispatch.dylib
/usr/lib/system/libdyld.dylib
/usr/lib/system/libkeymgr.dylib
/usr/lib/system/libmacho.dylib
/usr/lib/system/libquarantine.dylib
/usr/lib/system/libremovefile.dylib
/usr/lib/system/libsystem_asl.dylib
/usr/lib/system/libsystem_blocks.dylib
/usr/lib/system/libsystem_c.dylib
/usr/lib/system/libsystem_collections.dylib
/usr/lib/system/libsystem_configuration.dylib
/usr/lib/system/libsystem_containermanager.dylib
/usr/lib/system/libsystem_coreservices.dylib
/usr/lib/system/libsystem_darwin.dylib
/usr/lib/system/libsystem_darwindirectory.dylib
/usr/lib/system/libsystem_dnssd.dylib
/usr/lib/system/libsystem_eligibility.dylib
/usr/lib/system/libsystem_featureflags.dylib
/usr/lib/system/libsystem_info.dylib
/usr/lib/system/libsystem_kernel.dylib
/usr/lib/system/libsystem_m.dylib
/usr/lib/system/libsystem_malloc.dylib
/usr/lib/system/libsystem_networkextension.dylib
/usr/lib/system/libsystem_notify.dylib
/usr/lib/system/libsystem_platform.dylib
/usr/lib/system/libsystem_pthread.dylib
/usr/lib/system/libsystem_sandbox.dylib
/usr/lib/system/libsystem_sanitizers.dylib
/usr/lib/system/libsystem_secinit.dylib
/usr/lib/system/libsystem_symptoms.dylib
/usr/lib/system/libsystem_trace.dylib
/usr/lib/system/libsystem_trial.dylib
/usr/lib/system/libunwind.dylib
/usr/lib/system/libxpc.dylib
После завершения из монитора терминал напечатал ничего, код завершения 143.

## Программа на Python
Имя процесса в мониторе: 26845, PID 26845, память Физическая память: 17,6 МБ. Виртуальная память: 466,11 ГБ. Совместная память: 5,4 МБ. Собственная память: 7,9 МБ.
Памяти больше, чем у программы на C, примерно в 23 раз.
Общая библиотека у программ на C и Python: libSystem.B.dylib (libc).
Код завершения при обычном выходе: exit code: 0.

## Помощник ИИ (Р1)
Запрос: «Объясни программу hello.c по строкам». Одно место, где ответ точнее или менее точен, чем глава 0.1: ___.


ИИ: использовала для подсчета во сколько раз у Python памяти больше чем у праграммы на С
