import feedparser
import logging

logger = logging.getLogger(__name__)

class BloggerRSSFetcher:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
    
    def fetch_posts(self, label: str = None, max_results: int = 10):
        """Получает посты из Blogger"""
        if label:
            url = f"{self.base_url}/-/{label}?alt=rss&max-results={max_results}"
        else:
            url = f"{self.base_url}?alt=rss&max-results={max_results}"
        
        try:
            feed = feedparser.parse(url)
            
            if feed.bozo:
                logger.warning(f"Ошибка RSS: {feed.bozo_exception}")
                return []
            
            posts = []
            for entry in feed.entries:
                post = {
                    'id': entry.get('id', ''),
                    'title': entry.get('title', ''),
                    'link': entry.get('link', ''),
                    'content': self._extract_content(entry),
                    'summary': entry.get('summary', ''),
                    'published': entry.get('published', ''),
                    'author': entry.get('author', ''),
                    'labels': [tag.term for tag in entry.get('tags', [])]
                }
                posts.append(post)
            
            logger.info(f"Получено {len(posts)} постов" + 
                       (f" с меткой '{label}'" if label else ""))
            return posts
            
        except Exception as e:
            logger.error(f"Ошибка: {e}")
            return []
    
    def _extract_content(self, entry):
        """Извлекает контент"""
        if 'content' in entry:
            for content in entry.content:
                return content.value
        return entry.get('summary', '')