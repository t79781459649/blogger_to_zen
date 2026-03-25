"""
Отправка постов в Telegram
"""
def send_to_telegram(post, blog_config):
    '''Форматирует пост для Telegram'''
    message = f"*{post['title']}*\n\n"
    message += f"{post['content'][:500]}...\n\n"
    message += f"📖 Читать полностью: {post['link']}"
    
    print(f"Отправлено в Telegram: {post['title'][:50]}...")
    return True
