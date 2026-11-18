from pathlib import Path
print('Корпоративное приложение: версия 1.5')
print('Список модулей:', sorted(x.name for x in (Path(__file__).parent/'modules').glob('*.txt')))
