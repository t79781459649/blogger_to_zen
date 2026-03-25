"""
Замена YouTube на Rutube в контенте
"""
import re

class YouTubeReplacer:
    def __init__(self):
        self.patterns = [
            # YouTube embed
            (r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"', 
             r'src="https://rutube.ru/embed/\1"'),
            
            # YouTube watch links
            (r'href="https?://(?:www\.)?youtube\.com/watch\?v=([^&"]+)"',
             r'href="https://rutube.ru/video/\1/"'),
            
            # Short youtu.be links
            (r'href="https?://youtu\.be/([^"/]+)"',
             r'href="https://rutube.ru/video/\1/"')
        ]
    
    def replace(self, html_content: str) -> str:
        """Заменяет YouTube ссылки на Rutube"""
        if not html_content:
            return html_content
        
        result = html_content
        for pattern, replacement in self.patterns:
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        return result
    
    def find_youtube_links(self, html_content: str) -> list:
        """Находит все YouTube ссылки в тексте"""
        youtube_patterns = [
            r'youtube\.com/embed/([^"\s]+)',
            r'youtube\.com/watch\?v=([^&"\s]+)',
            r'youtu\.be/([^"\s]+)'
        ]
        
        links = []
        for pattern in youtube_patterns:
            matches = re.findall(pattern, html_content, re.IGNORECASE)
            links.extend([f"https://youtube.com/watch?v={m}" for m in matches])
        
        return links