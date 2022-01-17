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
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    news_urls = []
    selector = Selector(text=html_content)
    css_query = 'main .tec--card__title__link::attr(href)'
    news_urls = selector.css(css_query).getall()

    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    query = '.tec--btn::attr(href)'

    next_button_url = selector.css(query).get()
    if next_button_url == '':
        return None
    return next_button_url


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
