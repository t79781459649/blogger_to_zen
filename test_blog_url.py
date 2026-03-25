#!/usr/bin/env python3
"""
Тестирование нового URL блога
"""
import feedparser
from datetime import datetime

def test_blog_url():
    """Тестирует доступность блога и RSS"""
    test_urls = [
        'https://blog.roses-crimea.ru/feeds/posts/default',
        'https://blog.roses-crimea.ru/feeds/posts/default?alt=rss',
        'https://blog.roses-crimea.ru/feeds/posts/default?alt=rss&max-results=5'
    ]
    
    print("=" * 70)
    print("ТЕСТ ДОСТУПНОСТИ БЛОГА")
    print(f"Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    for url in test_urls:
        print(f"\n?? Тестируем URL: {url}")
        
        try:
            feed = feedparser.parse(url)
            
            print(f"   Статус: {feed.get('status', 'N/A')}")
            print(f"   Версия: {feed.get('version', 'N/A')}")
            
            if feed.bozo:
                print(f"   ??  Предупреждение: {feed.bozo_exception}")
            
            print(f"   Постов в RSS: {len(feed.entries)}")
            
            if feed.entries:
                print(f"   Последний пост:")
                print(f"      Заголовок: {feed.entries[0].title[:80]}...")
                print(f"      Дата: {feed.entries[0].get('published', 'N/A')}")
                
                # Показываем метки (если есть)
                if hasattr(feed.entries[0], 'tags'):
                    labels = [tag.term for tag in feed.entries[0].tags[:5]]
                    print(f"      Метки: {', '.join(labels)}")
            
            # Проверяем структуру
            print(f"   Поля в RSS: {list(feed.keys())}")
            
        except Exception as e:
            print(f"   ? ОШИБКА: {e}")
    
    print("\n" + "=" * 70)
    print("РЕКОМЕНДАЦИИ:")
    print("1. Если 'Постов в RSS' > 0 - блог доступен")
    print("2. Если видите метки - фильтрация по label будет работать")
    print("3. Используйте URL без ошибок в config.py")
    print("=" * 70)

if __name__ == "__main__":
    test_blog_url()