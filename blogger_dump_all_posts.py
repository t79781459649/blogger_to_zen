# blogger_dump_all_posts.py

"""
Скачивает ВСЕ посты из Google Blogger
и сохраняет каждый пост в отдельный HTML-файл.

Python 3.12+
Без API, без ключей, через Atom feed.
"""

import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
import html
import os
import re
import time

# ================== НАСТРОЙКИ ==================

BLOG_URL = "https://blogname.blogspot.com"   # ← ИЗМЕНИ
OUTPUT_DIR = "blogger_dump"                  # папка для сохранения
POSTS_PER_PAGE = 150                         # максимум у Blogger

SLEEP_SECONDS = 1                            # пауза, чтобы не злить Google

# =================================================


def safe_filename(text: str) -> str:
    """Делает безопасное имя файла"""
    text = re.sub(r"[^\w\-]+", "_", text)
    return text.strip("_")[:80]


def fetch(url: str) -> bytes:
    """Скачивает URL"""
    with urllib.request.urlopen(url) as r:
        return r.read()


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    start_index = 1
    total_saved = 0

    ns = {"atom": "http://www.w3.org/2005/Atom"}

    while True:
        feed_url = (
            f"{BLOG_URL}/feeds/posts/default"
            f"?alt=atom"
            f"&start-index={start_index}"
            f"&max-results={POSTS_PER_PAGE}"
        )

        print("Читаю:", feed_url)
        data = fetch(feed_url)

        root = ET.fromstring(data)
        entries = root.findall("atom:entry", ns)

        if not entries:
            break

        for entry in entries:
            title_el = entry.find("atom:title", ns)
            content_el = entry.find("atom:content", ns)
            published_el = entry.find("atom:published", ns)
            link_el = entry.find("atom:link[@rel='alternate']", ns)

            title = title_el.text if title_el is not None else "no_title"
            content = content_el.text if content_el is not None else ""
            link = link_el.attrib["href"] if link_el is not None else ""

            date_raw = published_el.text if published_el is not None else ""
            date = datetime.fromisoformat(date_raw.replace("Z", "+00:00"))
            date_str = date.strftime("%Y-%m-%d")

            filename = f"{date_str}__{safe_filename(title)}.html"
            path = os.path.join(OUTPUT_DIR, filename)

            html_page = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
</head>
<body>

<h1>{html.escape(title)}</h1>
<p><em>{date.isoformat()}</em></p>
<p><a href="{link}">{link}</a></p>
<hr>

{content}

</body>
</html>
"""

            with open(path, "w", encoding="utf-8") as f:
                f.write(html_page)

            total_saved += 1
            print("Сохранено:", filename)

        start_index += POSTS_PER_PAGE
        time.sleep(SLEEP_SECONDS)

    print(f"\nГОТОВО. Всего сохранено: {total_saved} постов")


if __name__ == "__main__":
    main()