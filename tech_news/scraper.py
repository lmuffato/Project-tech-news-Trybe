import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None

    if response.status_code != 200:
        return None

    return response.text


# Requisito 2
def scrape_novidades(html_content):
    content = Selector(html_content)
    # Fonte: https://parsel.readthedocs.io/en/latest/usage.html
    news_list = content.css("h3.tec--card__title a::attr(href)").getall()
    return news_list


# Requisito 3
def scrape_next_page_link(html_content):
    content = Selector(html_content)
    next_page_selector = content.css("a.tec--btn::attr(href)").get()
    return next_page_selector


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
