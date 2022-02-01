import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        else:
            return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    # seletor css do tecmundo: h3.tec--card__title  a.tec--card__title__link
    news_links = selector.css(
        'h3.tec--card__title a.tec--card__title__link::attr(href)'
        ).getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    # seletor css do tecmundo:
    # a.tec--btn.tec.btn--lg.tec--btn
    next_link = selector.css('a.tec--btn--lg::attr(href)').get()
    return next_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
