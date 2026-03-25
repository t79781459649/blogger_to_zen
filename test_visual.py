#!/usr/bin/env python3
"""
ВИЗУАЛЬНАЯ ПРОВЕРКА пайплайна
"""
import os
import json
from datetime import datetime

def show_posts_structure():
    """Показывает структуру полученных постов"""
    print("=" * 70)
    print("ВИЗУАЛЬНАЯ ПРОВЕРКА ПАЙПЛАЙНА")
    print("=" * 70)
    
    # Тестовые данные (имитация того, что получим)
    test_posts = [
        {
            'id': 'post_123',
            'title': 'Sharbat-e-Ghulab (Rooh Afza) Gulab Sharbat Recipe',
            'link': 'https://blog.roses-crimea.ru/2024/01/sharbat.html',
            'content': '<p>Рецепт персидского напитка... <iframe src="https://youtube.com/embed/abc123"></iframe></p>',
            'published': '2024-01-15T10:00:00',
            'labels': ['recipes', 'Персия', 'напитки'],
            'images': ['https://blog.roses-crimea.ru/image1.jpg']
        },
        {
            'id': 'post_456',
            'title': 'Масло шиповника - делаем сами',
            'link': 'https://blog.roses-crimea.ru/2024/01/rose-oil.html',
            'content': '<p>Как сделать масло шиповника дома... <a href="https://youtu.be/xyz789">Смотрите видео</a></p>',
            'published': '2024-01-14T15:30:00',
            'labels': ['шиповник', 'масло', 'рецепт'],
            'images': ['https://blog.roses-crimea.ru/oil.jpg']
        }
    ]
    
    print("\n📝 ПОЛУЧЕННЫЕ СТАТЬИ ИЗ BLOGGER:")
    print("-" * 70)
    
    for i, post in enumerate(test_posts, 1):
        print(f"\n{i}. {post['title']}")
        print(f"   🔗 Ссылка: {post['link']}")
        print(f"   📅 Дата: {post['published']}")
        print(f"   🏷️  Метки: {', '.join(post['labels'])}")
        
        # Проверяем наличие YouTube
        youtube_in_content = 'youtube' in post['content'].lower() or 'youtu.be' in post['content'].lower()
        if youtube_in_content:
            print(f"   ⚠️  Содержит YouTube ссылки")
        
        # Проверяем изображения
        if post.get('images'):
            print(f"   🖼️  Изображений: {len(post['images'])}")
            print(f"      Первое: {post['images'][0]}")
    
    # Показываем КАК будет обработан контент
    print("\n" + "=" * 70)
    print("🔧 ОБРАБОТКА КОНТЕНТА (что будет сделано):")
    print("-" * 70)
    
    for i, post in enumerate(test_posts, 1):
        print(f"\n{i}. {post['title'][:40]}...")
        
        # 1. Замена YouTube на Rutube
        if 'youtube' in post['content'].lower():
            processed = post['content'].replace('youtube.com', 'rutube.ru')
            processed = processed.replace('youtu.be', 'rutube.ru')
            print(f"   ✅ YouTube → Rutube: заменено")
        else:
            print(f"   ✅ YouTube нет, оставляем как есть")
        
        # 2. Извлечение изображений
        if post.get('images'):
            print(f"   🖼️  Изображения: будут сохранены локально")
        
        # 3. Теги для Дзен
        tags = post['labels'] + ['розы', 'крым', 'рецепты']
        print(f"   🏷️  Теги для Дзен: {', '.join(tags[:5])}...")
        
        # 4. Подборки Дзен
        if 'рецепт' in post['labels'] or 'recipes' in post['labels']:
            print(f"   📚 Подборка Дзен: «Рецепты с розами»")
        elif 'шиповник' in post['labels']:
            print(f"   📚 Подборка Дзен: «Здоровье и розы»")
        else:
            print(f"   📚 Подборка Дзен: «Крымские розы»")
    
    # Где брать шорты
    print("\n" + "=" * 70)
    print("🎬 ШОРТЫ (10-15 секунд):")
    print("-" * 70)
    print("Источники шортов:")
    print("1. 📁 Папка `shorts/` - положите туда видеофайлы")
    print("2. 📝 Конфиг `shorts_list.txt` - список ссылок на видео")
    print("3. 🎞️  Вырезать из длинных видео (будет в следующих версиях)")
    print("\nФормат `shorts_list.txt`:")
    print("  https://rutube.ru/video/123456/  # Цветение розы")
    print("  https://rutube.ru/video/789012/  # Приготовление шарбата")
    print("  /local/path/to/shorts/rose_bloom.mp4  # Локальный файл")
    
    # Теги для индекса
    print("\n" + "=" * 70)
    print("🔍 ТЕГИ ДЛЯ ИНДЕКСАЦИИ (SEO):")
    print("-" * 70)
    
    seo_tags = {
        'recipes': ['рецепт с розами', 'розовый шарбат', 'персидский напиток', 'кулинария с цветами'],
        'шиповник': ['масло шиповника', 'сделать самому', 'косметика своими руками', 'уход за кожей'],
        'общие': ['крымские розы', 'роза centifolia', 'выращивание роз', 'ароматерапия']
    }
    
    for category, tags in seo_tags.items():
        print(f"\n{category}:")
        for tag in tags:
            print(f"  • #{tag.replace(' ', '_')}")
    
    print("\n" + "=" * 70)
    print("📤 ЧТО ПРОИСХОДИТ ПРИ ПУБЛИКАЦИИ:")
    print("-" * 70)
    print("1. 📝 Получаем пост из Blogger")
    print("2. 🔧 Обрабатываем (YouTube→Rutube, очистка)")
    print("3. 🏷️  Добавляем теги для Дзен")
    print("4. 📅 Кладём в расписание (data/schedule.json)")
    print("5. ⏰ В нужное время:")
    print("   • 📲 Отправляем в Telegram (python-telegram-bot)")
    print("   • ✅ Telegram возвращает message_id (подтверждение)")
    print("   • 🌐 Telegram автоматически кросс-постит в Дзен")
    print("   • 💾 Сохраняем результат в logs/published.json")
    print("\nTelegram ОБЯЗАТЕЛЬНО публикует у себя, если нет ошибок!")
    print("Проверка: message_id в ответе = успешная публикация.")
    
    # Сохраняем пример для проверки
    os.makedirs('output_samples', exist_ok=True)
    sample_file = f"output_samples/sample_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    
    with open(sample_file, 'w', encoding='utf-8') as f:
        json.dump({
            'test_posts': test_posts,
            'seo_tags': seo_tags,
            'generated_at': datetime.now().isoformat()
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 Пример сохранён в: {sample_file}")
    print("=" * 70)

if __name__ == "__main__":
    show_posts_structure()