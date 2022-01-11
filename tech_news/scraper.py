import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    parsel_selector = Selector(html_content)
    list = []
    for news in parsel_selector.css("div.tec--list__item"):
        element_link = news.css("a.tec--card__title__link::attr(href)").get()
        list.append(element_link)
    return list


# Requisito 3
def scrape_next_page_link(html_content):
    parsel_selector = Selector(html_content)
    next_page_link = parsel_selector.css("a.tec--btn::attr(href)").get()
    if next_page_link:
        return next_page_link
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
