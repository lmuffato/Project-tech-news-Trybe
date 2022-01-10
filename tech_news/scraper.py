from parsel import Selector
import requests
from time import sleep


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        response = ""
    finally:
        if not response or response.status_code != 200:
            return None
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    URLS = selector.css(
        ".tec--list .tec--card__title__link::attr(href)"
    ).getall()
    return URLS if URLS else []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
