import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
    except (requests.ReadTimeout, requests.ConnectionError):
        return None

    time.sleep(1)


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    news_links_list = selector.css(
        '.tec--list .tec--card__title__link::attr(href)'
    ).getall()
    return news_links_list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
