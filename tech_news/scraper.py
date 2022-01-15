import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if (response.status_code != 200):
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2 src: https://parsel.readthedocs.io/en/latest/usage.html
def scrape_novidades(html_content):
    data = Selector(html_content)
    return data.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css("div.tec--list a.tec--btn::attr(href)").get()

    if next_page_link:
        return next_page_link
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
