# Requisito 1
import time
import requests
from parsel import Selector


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            raise requests.exceptions.HTTPError
        return response.text

    except requests.ReadTimeout:
        return None
    except requests.HTTPError:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    all_news = selector.css("h3.tec--card__title a::attr(href)").getall()
    return all_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_buttons = selector.css(
        "div.tec--list.tec--list--lg > "
        "a ::attr(href)").get()
    if not next_page_buttons:
        return None
    return next_page_buttons


# Requisito 4
def scrape_noticia(html_content):
    # selector = Selector(html_content)
    pass


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
