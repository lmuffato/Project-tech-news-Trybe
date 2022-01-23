from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        result = requests.get(url, timeout=3)
        time.sleep(1)
        if (result.status_code == 200):
            return result.text
        raise(ValueError)
    except (requests.Timeout, ValueError):
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    ref = '.tec--list__item article h3 a.tec--card__title__link::attr(href)'
    news = selector.css(ref).getall()
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
