#!/usr/bin/env python3
"""
Тестирование ВАШИХ меток Blogger
"""
import sys
import os
import json
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import BLOGGER_RSS_BASE, BLOGS
from src.rss_fetcher import BloggerRSSFetcher
from src.content_processor import ContentProcessor

def test_specific_labels():
    """Тестирует конкретные метки из вашего блога"""
    print("=" * 70)
    print("ТЕСТИРОВАНИЕ МЕТОК ВАШЕГО БЛОГА")
    print(f"Блог: {BLOGGER_RSS_BASE}")
    print(f"Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    fetcher = BloggerRSSFetcher(BLOGGER_RSS_BASE)
    processor = ContentProcessor()
    
    # Ваши реальные метки (из скриншота)
    my_labels = [
        'recipes',           # Рецепты
        'Centifolia',        # Столистная роза
        'Crimea',            # Крым
        'youtube',           # YouTube
        'масло шиповника',   # Масло шиповника
        'Турция',            # Турция
        'Персия',            # Персия
        'рецепт',            # Рецепт (русский)
        'GULKAND MILKSHAKE', # Конкретный рецепт
        'Джуладжубин',       # Джуладжубин
    ]
    
    results = {}
    
    print("\n?? Проверяем доступность меток:")
    print("-" * 70)
    
    for label in my_labels:
        print(f"\nМетка: '{label}'")
        
        try:
            posts = fetcher.fetch_posts(label=label, max_results=3)
            
            if posts:
                print(f"  ? НАЙДЕНО: {len(posts)} постов")
                
                # Обрабатываем первый пост
                if posts:
                    processed = processor.process(posts[0])
                    print(f"  ?? Пример: {processed['title'][:60]}...")
                    
                    # Показываем метки поста
                    if posts[0].get('labels'):
                        print(f"  ???  Метки поста: {', '.join(posts[0]['labels'][:5])}")
                    
                    # Сохраняем результат
                    results[label] = {
                        'available': True,
                        'count': len(posts),
                        'sample_title': posts[0]['title'],
                        'labels_in_post': posts[0].get('labels', [])
                    }
                else:
                    print(f"  ??  Пустой результат (метка может быть неверной)")
                    results[label] = {'available': False, 'error': 'empty'}
            
            else:
                print(f"  ? НЕ НАЙДЕНО")
                results[label] = {'available': False, 'error': 'not_found'}
                
        except Exception as e:
            print(f"  ? ОШИБКА: {str(e)[:100]}")
            results[label] = {'available': False, 'error': str(e)}
    
    # Тест из конфига
    print("\n" + "=" * 70)
    print("ТЕСТ КОНФИГУРАЦИИ (config.py):")
    print("-" * 70)
    
    for blog in BLOGS:
        label_display = blog['label'] or '(все посты)'
        print(f"\n?? {blog['name']} -> метка: '{label_display}'")
        
        posts = fetcher.fetch_posts(label=blog['label'], max_results=2)
        
        if posts:
            print(f"  ? Постов: {len(posts)}")
            for i, post in enumerate(posts, 1):
                print(f"  {i}. {post['title'][:70]}...")
        else:
            print(f"  ??  Постов не найдено")
    
    # Сохраняем результаты в файл
    output_file = "label_test_results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("\n" + "=" * 70)
    print("РЕЗУЛЬТАТЫ:")
    print("-" * 70)
    
    available = [label for label, data in results.items() if data.get('available')]
    unavailable = [label for label, data in results.items() if not data.get('available')]
    
    print(f"? Доступные метки ({len(available)}):")
    for label in available:
        count = results[label].get('count', 0)
        print(f"    {label} ({count} постов)")
    
    print(f"\n? Недоступные метки ({len(unavailable)}):")
    for label in unavailable[:10]:  # Показываем первые 10
        print(f"    {label}")
    
    if len(unavailable) > 10:
        print(f"   ... и еще {len(unavailable) - 10}")
    
    print("\n" + "=" * 70)
    print(f"?? Результаты сохранены в: {output_file}")
    print("=" * 70)
    
    # Рекомендации
    print("\n?? РЕКОМЕНДАЦИИ ДЛЯ config.py:")
    print("1. Используйте метки, которые показали '? Доступные'")
    print("2. Метки чувствительны к регистру: 'Centifolia' ? 'centifolia'")
    print("3. Русские метки работают, но проверьте точное написание")
    print("4. Для старта рекомендую:")
    print("   - recipes (рецепты)")
    print("   - Centifolia (столистная роза)")
    print("   - youtube (видео)")

if __name__ == "__main__":
    test_specific_labels()