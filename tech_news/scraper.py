import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        request = requests.get(url, timeout=3)
        time.sleep(1)
        if request.status_code == 200:
            return request.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    if selector:
        return selector.css(
                "h3.tec--card__title a.tec--card__title__link::attr(href)"
                ).getall()
    else:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    more = selector.css("div.tec--list a.tec--btn::attr(href)").get()
    if more:
        return more
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
