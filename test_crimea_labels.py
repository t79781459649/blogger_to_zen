#!/usr/bin/env python3
"""
Тестирование меток для блога Roses-Crimea
"""
import feedparser
from datetime import datetime

def test_labels():
    """Тестирует конкретные метки вашего блога"""
    
    # Базовый URL ВАШЕГО блога
    BASE_URL = "https://blog.roses-crimea.ru/feeds/posts/default"
    
    # Метки из вашего блога (на основе скриншотов)
    TEST_LABELS = [
        # Основные категории
        "recipes",           # Рецепты
        "Centifolia",        # Столистная роза
        "Crimea",            # Крым
        "youtube",           # YouTube
        "масло шиповника",   # Масло шиповника
        "Турция",            # Турция
        "Персия",            # Персия
        "рецепт",            # Рецепт
        "GULKAND MILKSHAKE", # Конкретный рецепт
        "Джуладжубин",       # Джуладжубин
        
        # Популярные теги из вашего блога
        "Rose Centifolia",
        "Roses",
        "Crimeo", 
        "David Austin",
        "масло",
        "шиповник",
        
        # Проверка чувствительности к регистру
        "centifolia",  # строчные буквы
        "Centifolia",  # с заглавной
        "CENTIFOLIA",  # заглавные
    ]
    
    print("=" * 70)
    print("ТЕСТ МЕТОК БЛОГА: Roses-Crimea.ru")
    print(f"Базовый URL: {BASE_URL}")
    print(f"Время теста: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    results = {}
    
    for label in TEST_LABELS:
        # Формируем URL с меткой
        if label:
            rss_url = f"{BASE_URL}/-/{label}?alt=rss&max-results=5"
        else:
            rss_url = f"{BASE_URL}?alt=rss&max-results=5"
        
        print(f"\n🔍 Метка: '{label}'")
        print(f"   URL: {rss_url}")
        
        try:
            feed = feedparser.parse(rss_url)
            
            if feed.bozo:
                print(f"   ⚠️  RSS ошибка: {feed.bozo_exception}")
            
            post_count = len(feed.entries)
            
            if post_count > 0:
                print(f"   ✅ НАЙДЕНО: {post_count} постов")
                
                # Показываем первый пост
                first_post = feed.entries[0]
                print(f"   📝 Пример: {first_post.title[:70]}...")
                
                # Показываем метки этого поста (если есть)
                if hasattr(first_post, 'tags'):
                    post_labels = [tag.term for tag in first_post.tags[:3]]
                    if post_labels:
                        print(f"   🏷️  Метки в посте: {', '.join(post_labels)}")
                
                results[label] = {
                    'available': True,
                    'count': post_count,
                    'sample_title': first_post.title,
                    'url': rss_url
                }
            else:
                print(f"   ❌ НЕ НАЙДЕНО постов")
                results[label] = {'available': False, 'count': 0}
                
        except Exception as e:
            print(f"   ❌ ОШИБКА: {str(e)[:100]}")
            results[label] = {'available': False, 'error': str(e)}
    
    # Анализ результатов
    print("\n" + "=" * 70)
    print("📊 СВОДКА РЕЗУЛЬТАТОВ:")
    print("=" * 70)
    
    available_labels = [label for label, data in results.items() 
                       if data.get('available')]
    
    unavailable_labels = [label for label, data in results.items() 
                         if not data.get('available')]
    
    print(f"\n✅ РАБОЧИЕ МЕТКИ ({len(available_labels)}):")
    for label in available_labels:
        count = results[label].get('count', 0)
        print(f"   • '{label}' - {count} постов")
    
    print(f"\n❌ НЕРАБОЧИЕ МЕТКИ ({len(unavailable_labels)}):")
    for label in unavailable_labels[:15]:
        print(f"   • '{label}'")
    
    if len(unavailable_labels) > 15:
        print(f"   ... и ещё {len(unavailable_labels) - 15}")
    
    # Проверка чувствительности к регистру
    print(f"\n🔤 ЧУВСТВИТЕЛЬНОСТЬ К РЕГИСТРУ:")
    if 'centifolia' in results and 'Centifolia' in results:
        lower = results['centifolia'].get('count', 0)
        upper = results['Centifolia'].get('count', 0)
        print(f"   'centifolia' (строчные): {lower} постов")
        print(f"   'Centifolia' (с заглавной): {upper} постов")
        if lower != upper:
            print(f"   ⚠️  Результаты разные! Используйте правильный регистр")
    
    print("\n" + "=" * 70)
    print("💡 РЕКОМЕНДАЦИИ ДЛЯ config.py:")
    print("1. Используйте только метки из раздела 'РАБОЧИЕ МЕТКИ'")
    print("2. Проверьте регистр меток")
    print("3. Начните с 2-3 меток для теста")
    print("=" * 70)
    
    # Сохраняем результаты
    import json
    with open('crimea_labels_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n📁 Результаты сохранены в: crimea_labels_results.json")
    
    return results

if __name__ == "__main__":
    test_labels()