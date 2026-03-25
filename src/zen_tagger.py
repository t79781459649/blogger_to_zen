"""
Генерация тегов для Дзен
"""
class ZenTagger:
    def __init__(self):
        self.base_tags = ['розы', 'крым', 'цветы', 'сад', 'рецепты']
        
        # Категории → теги
        self.category_tags = {
            'recipes': ['кулинария', 'напитки', 'персидская_кухня', 'шарбат'],
            'шиповник': ['здоровье', 'косметика', 'уход_за_кожей', 'натуральная_косметика'],
            'Centifolia': ['столистная_роза', 'эфирные_масла', 'ароматерапия'],
            'Crimea': ['крымские_розы', 'полуостров', 'юг_россии']
        }
    
    def generate_tags(self, post_labels: list, content: str = "") -> list:
        """Генерирует теги для Дзен"""
        tags = set(self.base_tags)
        
        # Добавляем теги по меткам
        for label in post_labels:
            label_lower = label.lower()
            for category, cat_tags in self.category_tags.items():
                if category.lower() in label_lower or label_lower in category.lower():
                    tags.update(cat_tags)
        
        # Анализ контента для дополнительных тегов
        content_lower = content.lower()
        if 'рецепт' in content_lower:
            tags.update(['готовка', 'пошаговый_рецепт', 'домашняя_кухня'])
        if 'масло' in content_lower:
            tags.update(['эфирные_масла', 'ароматерапия', 'натуральное'])
        if 'видео' in content_lower:
            tags.update(['видео', 'обучение', 'мастер_класс'])
        
        # Ограничиваем количество
        return list(tags)[:15]  # Дзен любит до 15 тегов