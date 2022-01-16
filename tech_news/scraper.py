import requests
from parsel import Selector
import time


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        response = None
    finally:
        if response is not None and response.status_code == 200:
            return response.text
        else:
            response = None
            return response


# Requisito 2
def scrape_novidades(html_content):
    list_url = []
    if html_content is not None or html_content != '':
        selector = Selector(text=html_content)
        links = selector.css("div.tec--card__info h3 a::attr(href)").getall()
        for link in links:
            list_url.append(link)

    return list_url


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
