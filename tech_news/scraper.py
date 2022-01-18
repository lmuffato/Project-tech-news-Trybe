import requests
import time
import parsel


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(text=html_content)
    array = []
    if len(array) == 0:
        return selector.css(
            ".tec--list .tec--card__title__link::attr(href)"
            ).getall()
    else:
        return array


def scrape_next_page_link(html_content):
    selector = parsel.Selector(text=html_content)
    next_page_url = selector.css(".tec--btn::attr(href)").get()
    if next_page_url != "":
        return next_page_url
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
