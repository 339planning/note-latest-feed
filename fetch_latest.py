import json
import re
import urllib.request
import xml.etree.ElementTree as ET

RSS_URL = "https://note.com/339planning/rss"
NS = {"media": "http://search.yahoo.com/mrss/"}


def strip_html(html):
    text = re.sub(r"<[^>]+>", "", html)
    text = text.replace("&nbsp;", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def main():
    req = urllib.request.Request(RSS_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as res:
        xml_bytes = res.read()

    root = ET.fromstring(xml_bytes)
    items = root.findall("./channel/item")[:3]

    latest = []
    for item in items:
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        description_html = item.findtext("description") or ""
        thumbnail = item.findtext("media:thumbnail", namespaces=NS) or ""
        latest.append({
            "title": title,
            "link": link,
            "thumbnail": thumbnail.strip(),
            "description": strip_html(description_html),
        })

    with open("latest3.json", "w", encoding="utf-8") as f:
        json.dump(latest, f, ensure_ascii=False, indent=2)

    print(f"{len(latest)}件書き出し完了")


if __name__ == "__main__":
    main()
