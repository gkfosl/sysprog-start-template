import argparse, hashlib, shutil, subprocess, sys, time
from pathlib import Path


def log(root, msg):
    line = f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}"
    print(line)
    with open(root / "update.log", "a", encoding="utf-8") as f:   # лог лежит вне app и user_data
        f.write(line + "\n")


def tree(root):
    """{относительный путь: sha256}. Сравниваем по содержимому, не по размеру/дате."""
    out = {}
    for p in sorted(root.rglob("*")):
        if p.is_file() or p.is_symlink():
            out[p.relative_to(root).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out



def smoke(app):
    r = subprocess.run([sys.executable, str(app / "main.py")], capture_output=True, text=True, timeout=30)
    return r.returncode == 0, (r.stdout + r.stderr).strip()


def recover(root, app, backup, staging):
    """Если прошлый запуск оборвали: чиним состояние до начала работы."""
    if staging.exists():
        shutil.rmtree(staging)
        log(root, "найден недокопированный staging от прерванного запуска — удалён")
    if not app.exists() and backup.exists():
        backup.rename(app)
        log(root, "app отсутствовал (обрыв при подмене) — восстановлен из бэкапа")


def rollback(root, app, backup):
    if not backup.exists():
        log(root, "ОТКАТ невозможен: бэкапа нет"); return 1
    failed = root / ".app_failed"
    if failed.exists(): shutil.rmtree(failed)
    if app.exists(): app.rename(failed)
    backup.rename(app)
    if failed.exists(): shutil.rmtree(failed)
    log(root, "откат выполнен: восстановлена предыдущая версия")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--installed", required=True, type=Path)
    ap.add_argument("--release", type=Path)
    ap.add_argument("--rollback", action="store_true")
    a = ap.parse_args()

    root = a.installed.resolve()
    app, backup, staging = root / "app", root / ".app_backup", root / ".app_new"
    recover(root, app, backup, staging)
    if a.rollback:
        return rollback(root, app, backup)

    src = (a.release / "app").resolve() if (a.release / "app").is_dir() else a.release.resolve()
    try:
        new, old = tree(src), tree(app)          # ошибка тут (нет/нечитаем исходный файл) = app не тронут
    except OSError as e:
        log(root, f"ОШИБКА: не могу прочитать исходники релиза: {e}. Установленная версия не изменена")
        return 2

    add = sorted(set(new) - set(old))
    rem = sorted(set(old) - set(new))
    chg = sorted(k for k in new if k in old and new[k] != old[k])
    if not (add or rem or chg):
        log(root, "уже актуально: изменений нет"); return 0
    log(root, f"план: добавить {add}, заменить {chg}, удалить {rem}")

    try:
        shutil.copytree(src, staging)            # 1. собираем новую версию рядом
        if tree(staging) != new:                 # 2. проверяем копию
            raise RuntimeError("хеши копии не совпали с релизом")
    except Exception as e:
        shutil.rmtree(staging, ignore_errors=True)
        log(root, f"ОШИБКА при копировании: {e}. Установленная версия не изменена"); return 2

    if backup.exists(): shutil.rmtree(backup)
    try:
        app.rename(backup)                       # 3. две быстрых операции переименования
        staging.rename(app)
    except OSError as e:                         # напр. Windows: файл занят запущенной программой
        if not app.exists() and backup.exists(): backup.rename(app)
        shutil.rmtree(staging, ignore_errors=True)
        log(root, f"ОШИБКА подмены (файлы заняты?): {e}. Откат, версия не изменена"); return 3

    ok, out = smoke(app)                         # 4. приложение должно запускаться
    if not ok:
        log(root, f"main.py не запустился после обновления: {out}")
        rollback(root, app, backup); return 4
    log(root, "обновление успешно. main.py вывод: " + out.replace("\n", " | "))
    return 0


if __name__ == "__main__":
    sys.exit(main())