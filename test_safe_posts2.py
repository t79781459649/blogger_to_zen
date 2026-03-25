#!/usr/bin/env python3
"""
ТЕСТОВЫЙ СКРИПТ: 5 безопасных постов для проверки системы
Тема: 'Мой куст столепестной - день N'
"""
import feedparser
import json
import os
from datetime import datetime
import html

def fetch_safe_posts():
    """Получает безопасные посты для теста"""
    print("=" * 60)
    print("ТЕСТОВЫЙ СБОР БЕЗОПАСНЫХ ПОСТОВ")
    print("=" * 60)
    
    # Безопасная метка (проверенная)
    SAFE_LABEL = "Centifolia"
    BLOG_URL = "https://blog.roses-crimea.ru/feeds/posts/default"
    
    # Формируем URL
    test_url = f"{BLOG_URL}/-/{SAFE_LABEL}?alt=rss&max-results=5"
    
    print(f"📡 Запрос: {test_url}")
    
    feed = feedparser.parse(test_url)
    
    if feed.bozo:
        print(f"⚠️  RSS ошибка: {feed.bozo_exception}")
        return []
    
    print(f"✅ Найдено постов: {len(feed.entries)}")
    
    safe_posts = []
    
    # Безопасные заголовки для 5 дней
    safe_titles = [
        "Мой куст столепестной розы - день первый наблюдений",
        "Столепестная роза: день второй, первые бутоны", 
        "День третий: как растёт лечебная роза в моём саду",
        "Наблюдения за розой Centifolia - день четвёртый",
        "Пятый день с моим кустом столепестной розы"
    ]
    
    for i, entry in enumerate(feed.entries[:5]):  # Берём максимум 5
        print(f"\n{i+1}. Исходный заголовок: {entry.title}")
        
        # Создаём безопасную версию
        safe_post = {
            'original_title': entry.title,
            'safe_title': safe_titles[i] if i < len(safe_titles) else f"Наблюдение за розой - день {i+1}",
            'original_link': entry.get('link', ''),
            'content': make_content_safe(entry.get('summary', '')),
            'published': entry.get('published', datetime.now().isoformat()),
            'test_day': i + 1,
            'has_youtube': 'youtube' in (entry.get('summary', '') + entry.get('title', '')).lower(),
            'labels': [tag.term for tag in entry.get('tags', [])],
            'is_test': True,
            'test_timestamp': datetime.now().isoformat()
        }
        
        # Добавляем короткий шорт (10 сек)
        safe_post['short_video'] = {
            'description': f"Куст столепестной розы, день {i+1}",
            'duration': 10,
            'tags': ['роза', 'садоводство', 'цветы', 'красота', 'природа'],
            'safe_hashtags': ['#роза', '#цветы', '#сад', '#природа', '#красота']
        }
        
        safe_posts.append(safe_post)
        
        print(f"   📝 Безопасный заголовок: {safe_post['safe_title']}")
        print(f"   🎬 Шорт: 10 сек, теги: {', '.join(safe_post['short_video']['tags'][:3])}")
        
        if safe_post['has_youtube']:
            print(f"   ⚠️  Исходный пост содержит YouTube - нужно заменить")
    
    return safe_posts

def make_content_safe(content):
    """Делает контент безопасным для публикации"""
    if not content:
        return "Наблюдения за ростом столепестной розы. Фото и видео процесса."
    
    # 1. Удаляем опасные слова
    dangerous_words = ['крым', 'санкц', 'полит', 'войн', 'границ']
    safe_content = content
    for word in dangerous_words:
        # Заменяем опасные слова на нейтральные
        safe_content = safe_content.replace(word, '[нейтр]')
    
    # 2. Очищаем HTML
    safe_content = html.unescape(safe_content)
    
    # 3. Ограничиваем длину
    if len(safe_content) > 500:
        safe_content = safe_content[:500] + "..."
    
    # 4. Добавляем безопасный префикс
    safe_content = f"Личные наблюдения за растением. {safe_content}"
    
    return safe_content

def save_test_posts(posts):
    """Сохраняет тестовые посты в папку"""
    test_dir = "test_run_" + datetime.now().strftime("%Y%m%d_%H%M")
    os.makedirs(test_dir, exist_ok=True)
    
    print(f"\n💾 Сохраняю посты в папку: {test_dir}")
    
    # Сохраняем каждый пост отдельно
    for i, post in enumerate(posts):
        day_dir = os.path.join(test_dir, f"day_{i+1}")
        os.makedirs(day_dir, exist_ok=True)
        
        # JSON с данными
        post_file = os.path.join(day_dir, "post_data.json")
        with open(post_file, 'w', encoding='utf-8') as f:
            json.dump(post, f, ensure_ascii=False, indent=2)
        
        # TXT для ручной проверки
        txt_file = os.path.join(day_dir, "post_for_telegram.txt")
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(f"Заголовок: {post['safe_title']}\n")
            f.write(f"День теста: {post['test_day']}\n")
            f.write(f"Тег: [ТЕСТ_РОЗА_ДЕНЬ{post['test_day']}]\n\n")
            f.write(f"{post['content']}\n\n")
            f.write(f"🎬 Шорт (10 сек): {post['short_video']['description']}\n")
            f.write(f"Теги шорта: {', '.join(post['short_video']['tags'])}\n")
            f.write(f"Хештеги: {', '.join(post['short_video']['safe_hashtags'])}\n\n")
            f.write(f"📅 Дата: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"✅ Это тестовая публикация\n")
        
        print(f"   День {i+1}: сохранён в {day_dir}/")
    
    # Общий файл со всеми постами
    all_posts_file = os.path.join(test_dir, "all_test_posts.json")
    with open(all_posts_file, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    
    return test_dir

def generate_telegram_test_script(posts, test_dir):
    """Генерирует скрипт для отправки в Telegram"""
    script_content = """#!/usr/bin/env python3
"""
    script_content += f'''
"""
ТЕСТОВАЯ ОТПРАВКА В TELEGRAM
Папка с тестами: {test_dir}
"""
import os
import json
import telebot
from datetime import datetime

# === НАСТРОЙКИ ===
# ВАШ ТОКЕН БУДЕТ ЗДЕСЬ
TELEGRAM_TOKEN = "ВАШ_TELEGRAM_BOT_TOKEN_ЗДЕСЬ"
CHANNEL_ID = "@ВАШ_КАНАЛ_ИЛИ_ЧАТ_ID"

# Инициализация бота
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def send_test_post(day_number):
    """Отправляет тестовый пост"""
    post_file = os.path.join("{test_dir}", f"day_{{day_number}}", "post_data.json")
    
    if not os.path.exists(post_file):
        print(f"❌ Файл для дня {{day_number}} не найден")
        return False
    
    with open(post_file, 'r', encoding='utf-8') as f:
        post = json.load(f)
    
    print(f"🚀 Отправляю тестовый пост: день {{day_number}}")
    print(f"   Заголовок: {{post['safe_title']}}")
    
    try:
        # Формируем сообщение
        message = f"[ТЕСТ] {{post['safe_title']}}\\n\\n"
        message += f"{{post['content']}}\\n\\n"
        message += f"🎬 {{post['short_video']['description']}}\\n"
        message += f"📅 {{datetime.now().strftime('%Y-%m-%d %H:%M')}}\\n"
        message += f"#тест #роза #садоводство"
        
        # Отправляем в Telegram
        sent_message = bot.send_message(CHANNEL_ID, message, parse_mode='Markdown')
        
        print(f"✅ Успешно отправлено! Message ID: {{sent_message.message_id}}")
        
        # Сохраняем результат
        result_file = os.path.join("{test_dir}", f"day_{{day_number}}", "telegram_result.json")
        result = {{
            'success': True,
            'message_id': sent_message.message_id,
            'date': datetime.now().isoformat(),
            'channel': CHANNEL_ID
        }}
        
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка отправки: {{e}}")
        return False

def main():
    """Основная функция"""
    print("=" * 60)
    print("ТЕСТОВАЯ ОТПРАВКА В TELEGRAM")
    print("=" * 60)
    
    # Проверка токена
    if TELEGRAM_TOKEN == "ВАШ_TELEGRAM_BOT_TOKEN_ЗДЕСЬ":
        print("❌ Сначала получите токен бота!")
        print("1. Напишите @BotFather в Telegram")
        print("2. Команда: /newbot")
        print("3. Пришлите мне токен")
        return
    
    print(f"📁 Тестовая папка: {test_dir}")
    print(f"📤 Канал/чат: {{CHANNEL_ID}}")
    print()
    
    # Отправляем первый тестовый пост
    print("Начинаем тест...")
    success = send_test_post(1)
    
    if success:
        print("\\n✅ Первый тестовый пост отправлен!")
        print("Подождите 24 часа, проверьте:")
        print("1. Пост появился в канале?")
        print("2. Его не удалили?")
        print("3. Кросс-постинг в Дзен работает?")
        print("\\nЕсли всё ок - запустите снова и отправьте день 2:")
        print("send_test_post(2)")
    else:
        print("\\n❌ Тест не прошёл. Проверьте токен и настройки.")

if __name__ == "__main__":
    main()
'''
    
    script_file = os.path.join(test_dir, "send_to_telegram.py")
    with open(script_file, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print(f"\n📄 Скрипт для Telegram: {script_file}")
    
    # Инструкция
    instructions = f"""
    
    ИНСТРУКЦИЯ ДЛЯ ТЕСТА:
    ====================
    
    1. ЗАПУСТИТЕ сбор тестовых постов:
       python test_safe_posts.py
    
    2. ПОЛУЧИТЕ токен бота Telegram:
       - Напишите @BotFather в Telegram
       - Команда: /newbot
       - Назовите бота: "RosesTestBot" или подобное
       - Получите токен (выглядит как: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz)
    
    3. НАСТРОЙТЕ бота:
       - Добавьте бота в ваш канал как администратора
       - Укажите ID канала в скрипте
    
    4. ЗАПУСТИТЕ тестовую отправку:
       python {test_dir}/send_to_telegram.py
    
    5. ПРОВЕРЬТЕ результат через 24 часа
    
    Папка с тестами: {test_dir}
    """
    
    print(instructions)
    
    # Сохраняем инструкцию в файл
    instr_file = os.path.join(test_dir, "README_ТЕСТ.txt")
    with open(instr_file, 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    return script_file

def main():
    """Основная функция"""
    print("🌹 ТЕСТОВЫЙ ПРОГОН: 5 безопасных дней с розой")
    
    # 1. Получаем посты
    posts = fetch_safe_posts()
    
    if not posts:
        print("❌ Не удалось получить посты для теста")
        return
    
    # 2. Сохраняем
    test_dir = save_test_posts(posts)
    
    # 3. Генерируем скрипт для Telegram
    generate_telegram_test_script(posts, test_dir)
    
    print("\n" + "=" * 60)
    print("✅ ТЕСТОВЫЕ ПОСТЫ ПОДГОТОВЛЕНЫ!")
    print("=" * 60)
    print(f"\nСледующие шаги:")
    print(f"1. Проверьте папку: {test_dir}/")
    print(f"2. Получите токен бота Telegram у @BotFather")
    print(f"3. Отредактируйте файл: {test_dir}/send_to_telegram.py")
    print(f"4. Запустите тестовую отправку")
    print(f"\n⚡ Первый пост отправим сразу для проверки!")
    print("=" * 60)

if __name__ == "__main__":
    main()