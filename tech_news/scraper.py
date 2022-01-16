from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, verify=False, timeout=3)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.exceptions.ReadTimeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    return selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    link = selector.css("div.tec--list a.tec--btn::attr(href)").get()

    if link:
        return link
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
