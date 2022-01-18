import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):

    try:
        res = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if res.status_code == 200:
        return res.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    response = Selector(html_content)
    response_links = response.css(
        "div.tec--list__item > article > div > h3 > a::attr(href)"
    ).getall()
    return response_links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
