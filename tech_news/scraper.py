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
        url = card.css('a::attr(href)').get()
        news.append(url)

    return news


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
