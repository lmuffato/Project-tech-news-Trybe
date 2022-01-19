import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    response = requests.get(url)
    time.sleep(1)
    if response.status_code == 200:
        return response.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    array = []
    if len(array) == 0:
        return selector.css(
            ".tec--list .tec--card__title__link::attr(href)"
            ).getall()
    else:
        return array


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
