#  blogger_atom_to_dzen_rss.py

"""
Преобразование Atom / RSS от Google Blogger
в RSS 2.0, совместимый с Яндекс Дзен.

Python 3.13
Без сторонних библиотек.
"""

import xml.etree.ElementTree as ET
from email.utils import format_datetime
from datetime import datetime, timezone
import html

# ====== НАСТРОЙКИ ======

INPUT_FILE = "blogger_atom.xml"     # входной файл (скачанный Atom Blogger)
OUTPUT_FILE = "dzen_rss.xml"         # выходной RSS для Дзена
CHANNEL_TITLE = "Название канала"
CHANNEL_LINK = "https://example.com"
CHANNEL_DESCRIPTION = "Описание канала для Дзена"


# ====== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ======

def parse_blogger_date(date_str: str) -> str:
    """
    Blogger даёт дату в ISO формате.
    Дзен требует RFC 822 (Wed, 02 Oct 2002 13:00:00 +0000)
    """
    dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    return format_datetime(dt)


def strip_html(text: str) -> str:
    """
    Убираем лишние экранирования.
    Сам HTML оставляем — Дзен его понимает.
    """
    return html.unescape(text or "")


# ====== ОСНОВНАЯ ЛОГИКА ======

def convert():
    tree = ET.parse(INPUT_FILE)
    root = tree.getroot()

    ns = {
        "atom": "http://www.w3.org/2005/Atom"
    }

    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = CHANNEL_TITLE
    ET.SubElement(channel, "link").text = CHANNEL_LINK
    ET.SubElement(channel, "description").text = CHANNEL_DESCRIPTION

    for entry in root.findall("atom:entry", ns):

        item = ET.SubElement(channel, "item")

        title = entry.find("atom:title", ns)
        ET.SubElement(item, "title").text = title.text if title is not None else ""

        link = entry.find("atom:link[@rel='alternate']", ns)
        ET.SubElement(item, "link").text = link.attrib["href"] if link is not None else ""

        guid = ET.SubElement(item, "guid", isPermaLink="false")
        guid.text = entry.find("atom:id", ns).text

        published = entry.find("atom:published", ns)
        if published is not None:
            ET.SubElement(item, "pubDate").text = parse_blogger_date(published.text)

        content = entry.find("atom:content", ns)
        description = ET.SubElement(item, "description")
        description.text = strip_html(content.text if content is not None else "")

    tree_out = ET.ElementTree(rss)
    tree_out.write(OUTPUT_FILE, encoding="utf-8", xml_declaration=True)

    print("Готово. RSS для Дзена создан:", OUTPUT_FILE)


# ====== ЗАПУСК ======

if __name__ == "__main__":
    convert()