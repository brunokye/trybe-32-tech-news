import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        page = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )

        if page.status_code != 200:
            return None

        return page.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    cards = selector.css(".entry-preview")

    news = []

    for card in cards:
        url = card.css("a::attr(href)").get()
        news.append(url)

    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    new_url = selector.css("a.next::attr(href)").get()

    return new_url


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    reading_time = int(
        selector.css(".meta-reading-time::text").get().split()[0]
    )
    summary = "".join(
        selector.css("div.entry-content >p:first-of-type *::text").getall()
    ).strip()
    category = selector.css(".label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
