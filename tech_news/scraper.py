import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        my_request = requests.get(url, timeout=3)
        if my_request.status_code not in [requests.codes.ok]:
            return None
        return my_request.text
    except requests.Timeout:
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_selector = ".tec--list .tec--card__title__link::attr(href)"
    return selector.css(news_selector).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
