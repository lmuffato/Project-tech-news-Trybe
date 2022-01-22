import requests
import time
from parsel import Selector


# Requisito 1
limit_time = 3
status_ok = 200


def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        res = requests.get(url, timeout=limit_time)
        if (res.status_code == status_ok):
            return res.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url_list = selector.css('h3.tec--card__title a::attr(href)').getall()
    if (url_list):
        return url_list
    return []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css('div.tec--list a.tec--btn::attr(href)').get()
    if (not next_page):
        return None
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
