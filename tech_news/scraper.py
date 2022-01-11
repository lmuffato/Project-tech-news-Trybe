import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        # recurso demora muito a responder
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        # vamos fazer uma nova requisição
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    list = []
    selector = Selector(text=html_content)

    for url in selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall():
        list.append(url)

    return list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
