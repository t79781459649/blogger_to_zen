import os
# config.py - УПРОЩЕННАЯ ВЕРСИЯ БЕЗ .env
# Убрали проблемную строку:
# from dotenv import load_dotenv
# load_dotenv()

# === ВАШ БЛОГ ===
BLOGGER_RSS_BASE = 'https://blog.roses-crimea.ru/feeds/posts/default'

# === РАБОЧИЕ МЕТКИ (из теста) ===
BLOGS = [
    # ТОЛЬКО те, что реально работают:
    {
        'name': 'recipes',
        'label': 'recipes',  # ✅ 5 постов
        'enabled': True,
        'tags': ['рецепты', 'розы', 'крым']
    },
    {
        'name': 'centifolia',
        'label': 'Centifolia',  # ✅ 2 поста (с заглавной!)
        'enabled': True,
        'tags': ['centifolia', 'роза', 'крым']
    },
    {
        'name': 'proekt_r',
        'label': 'Проект R',  # Для тестирования
        'enabled': True,
        'tags': ['проект r', 'тест']
    },
    # ... остальные метки
]

# === TELEGRAM ===
TELEGRAM_BOT_TOKEN = ''  # Будет позже
TELEGRAM_CHANNEL = '@ваш_канал'

# === НАСТРОЙКИ ===
PUBLISHING = {
    'posts_per_day': 2,
    'min_interval_hours': 6,
}

CONTENT = {
    'replace_youtube': True,
    'archive_enabled': True,
}