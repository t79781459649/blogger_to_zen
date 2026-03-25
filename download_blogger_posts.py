#  download_blogger_posts.py

"""
Скачивает ВСЕ посты из Blogger
и сохраняет в папку внутри проекта.

Адаптировано под:
C:\Users\An\Documents\blogger-to-zen\.venv
Python 3.11 (embed) / 3.12 совместимо
"""

from blogger_rss_fetcher import BloggerRSSFetcher
from datetime import datetime
import os
import re
import html

# ================= НАСТРОЙКИ =================

BLOG_URL = "https://blogname.blogspot.com"   # ← ОБЯЗАТЕЛЬНО ИЗМЕНИ

# папка будет внутри проекта
BASE_DIR = r"C:\Users\An\Documents\blogger-to-zen"
OUTPUT_DIR = os.path.join(BASE_DIR, "blogger_posts")

# ============================================


def safe_filename(text: str) -> str:
    """
    Делает безопасное имя файла:
    - убирает спецсимволы
    - ограничивает длину
    """
    text = re.sub(r"[^\w\-]+", "_", text)
    return text.strip("_")[:80]


def main():
    print("Старт загрузки...\n")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    fetcher = BloggerRSSFetcher(BLOG_URL)

    count = 0

    for post in fetcher.fetch_all_posts():

        # -------- данные поста --------

        title = post.title or "no_title"
        content = post.content or ""
        published = post.published
        link = post.link or ""

        # защита от None (редко, но бывает)
        if not published:
            published = datetime.now()

        date_str = published.strftime("%Y-%m-%d")

        filename = f"{date_str}__{safe_filename(title)}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # -------- HTML файл --------

        html_page = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
</head>
<body>

<h1>{html.escape(title)}</h1>
<p><em>{published.isoformat()}</em></p>
<p><a href="{link}">{link}</a></p>
<hr>

{content}

</body>
</html>
"""

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_page)

        count += 1
        print(f"[{count}] Сохранено: {filename}")

    print("\nГотово.")
    print(f"Всего постов: {count}")
    print(f"Папка: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()