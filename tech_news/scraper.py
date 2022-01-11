import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    link_selector = ".tec--list__item .tec--card__title__link::attr(href)"
    list = selector.css(link_selector).getall()
    if not list:
        return []
    else:
        return list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link_selector = ".tec--list .tec--btn.tec--btn--primary::attr(href)"
    next_page_link = selector.css(link_selector).get()
    if not next_page_link:
        return None
    else:
        return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
