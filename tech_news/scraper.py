import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    data = Selector(html_content)
    return data.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
        ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    see_more_news_btn = selector.css(".tec--list a.tec--btn::attr(href)").get()
    return see_more_news_btn


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
