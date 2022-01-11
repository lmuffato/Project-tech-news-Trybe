import requests
import time
from parsel import Selector

# Requisito 1


def fetch(url):
    try:
        time.sleep(1)
        data = requests.get(url, timeout=3)
        data.raise_for_status()
        return data.text
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    url_list = list()

    for url in selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall():
        url_list.append(url)

    return url_list

# Requisito 3


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    url = selector.css(".tec--list a.tec--btn::attr(href)").get()
    return url


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
