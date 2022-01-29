import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    list_news = selector.css(
        'h3.tec--card__title a.tec--card__title__link::attr(href)'
    ).getall()
    if len(list_news) == 0:
        return []
    return list_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_pag_url = selector.css('a.tec--btn::attr(href)').get()
    if next_pag_url == "":
        return None
    return next_pag_url


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
