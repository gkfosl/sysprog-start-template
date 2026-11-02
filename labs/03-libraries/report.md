# ЛР 3. Библиотеки программы

Система: 
ProductName:		macOS
ProductVersion:		27.0.1
BuildVersion:		26A434

## Библиотеки файла
Программа напечатала: ./libs: sqrt(2) = 1.414214
Команда для списка библиотек файла: otool -L libs
Библиотеки libs: /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1356.0.0)
Почему в списке нет отдельной математической библиотеки (или почему она есть): В macOS функции C, математика и системные вызовы собраны в одну библиотеку libSystem. Её загружает каждая программа macOS. Это динамическая компоновка
Где лежит интерпретатор Python (файл или библиотека):
/Library/Frameworks/Python.framework/Versions/3.13/Python (compatibility version 3.13.0, current version 3.13.0)
/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1351.0.0)

## Библиотеки процесса
PID Python: 8160
Библиотек в процессе до ctypes.CDLL: 204, после: 206
Загруженная библиотека и её полный путь: /usr/lib/libpcap.A.dylib
Функция вернула: b'libpcap version 1.10.1'

## Помощник ИИ (Р1)
Запрос: «Чем статическая компоновка отличается от динамической?». Совпал ли ответ с таблицей §2: ___.

ИИ: не использовал 
