# Создайте test_safe_posts.py
import feedparser

# Безопасная метка (уже тестировали - работает)
SAFE_LABEL = "Centifolia"  # ✅ Работает, медицинская, но не санкционная
BLOG_URL = "https://blog.roses-crimea.ru/feeds/posts/default"

print("=" * 50)
print("ТЕСТ: Безопасный сбор постов 'Centifolia'")
print("=" * 50)

# Формируем безопасный URL
test_url = f"{BLOG_URL}/-/{SAFE_LABEL}?alt=rss&max-results=3"

feed = feedparser.parse(test_url)
print(f"Найдено постов: {len(feed.entries)}")

for i, entry in enumerate(feed.entries, 1):
    print(f"\n{i}. {entry.title}")
    print(f"   Дата: {entry.get('published', 'N/A')}")
    
    # Безопасный превью (первые 100 символов)
    content = entry.get('summary', '')[:100]
    print(f"   Превью: {content}...")
    
    # Проверяем наличие YouTube (чтобы заменить)
    if 'youtube' in content.lower():
        print(f"   ⚠️  Содержит YouTube - нужно заменить на Rutube")
    
    print(f"   ✅ ГОТОВО для тестовой публикации")

print("\n" + "=" * 50)
print("РЕКОМЕНДАЦИЯ:")
print("1. Берём первые 2 поста")
print("2. Меняем заголовки на 'Мой куст столепестной - день N'")
print("3. Публикуем как ТЕСТ")
print("=" * 50)