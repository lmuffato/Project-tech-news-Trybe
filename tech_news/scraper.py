import time
import requests
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
    selector = Selector(html_content)
    link = "h3.tec--card__title a::attr(href)"
    data = selector.css(link).getall()

    return data


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    link = "a.tec--btn ::attr(href)"
    data = selector.css(link).get()

    return data


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
