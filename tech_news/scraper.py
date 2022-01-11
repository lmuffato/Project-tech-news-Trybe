import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url)
        if (response.status_code == 200):
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""

    selector = Selector(html_content)
    url_list = []
    for notice in selector.css("div.tec--list__item"):
        url = notice.css("a.tec--card__title__link::attr(href)").get()
        url_list.append(url)
    return url_list

# Requisito 3


def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
