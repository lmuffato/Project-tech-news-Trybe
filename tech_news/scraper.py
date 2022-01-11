import requests
import time
from parsel import Selector

# Requisito 1


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None

    if response.status_code != 200:
        return None
    else:
        return response.text


# Requisito 2


def scrape_novidades(html_content):
    _selector_ = Selector(text=html_content)

    urls = _selector_.css(
      "h3.tec--card__title a.tec--card__title__link::attr(href)"
      ).getall()

    return urls

# Requisito 2 foi entendindo utilizando o seguinte link:
# https://parsel.readthedocs.io/en/latest/usage.html#nesting-selectors

# Requisito 3


def scrape_next_page_link(html_content):
    _selector_ = Selector(text=html_content)

    next_url = _selector_.css(
      "a.tec--btn.tec--btn--lg.tec--btn-" +
      "-primary.z--mx-auto.z--mt-48::attr(href)"
      ).get()

    return next_url


# Requisito 4


def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5


def get_tech_news(amount):
    """Seu código deve vir aqui"""
