import sys
import os

print("=" * 50)
print("ПРОВЕРКА ОКРУЖЕНИЯ В VS CODE")
print("=" * 50)

# 1. Проверяем путь к Python
print(f"1. Python путь: {sys.executable}")

# 2. Проверяем версию
print(f"2. Версия Python: {sys.version}")

# 3. Проверяем, в виртуальном ли окружении
venv_path = sys.prefix
is_venv = "venv" in venv_path.lower() or ".venv" in venv_path.lower()
print(f"3. В виртуальном окружении: {'ДА' if is_venv else 'НЕТ'}")

# 4. Проверяем установленные пакеты (попробуем импортировать feedparser)
try:
    import feedparser
    print(f"4. Feedparser: УСТАНОВЛЕН (версия: {feedparser.__version__})")
except ImportError:
    print("4. Feedparser: НЕ УСТАНОВЛЕН")

print("=" * 50)
print("ЕСЛИ ВСЁ ХОРОШО:")
print("- Путь должен содержать '.venv'")
print("- Версия должна быть 3.11.x")
print("- Feedparser должен быть установлен")
print("=" * 50)