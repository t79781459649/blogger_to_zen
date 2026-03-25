import re
import html

class ContentProcessor:
    def process(self, post):
        """Обрабатывает пост"""
        processed = post.copy()
        
        # Очистка HTML
        if 'content' in processed:
            processed['content'] = self._clean_html(processed['content'])
        
        return processed
    
    def _clean_html(self, html_content):
        """Очищает HTML"""
        # Удаляем скрипты и стили
        cleaned = re.sub(r'<(script|style).*?>.*?</\1>', '', html_content, flags=re.DOTALL)
        # Декодируем HTML-сущности
        cleaned = html.unescape(cleaned)
        return cleaned