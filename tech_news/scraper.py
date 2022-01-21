import time
import requests
import parsel


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None

    if response.status_code != 200:
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    list = []
    selector = parsel.Selector(text=html_content)
    list = selector.css('main .tec--card__title__link::attr(href)').getall()

    return list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(text=html_content)
    next_page = selector.css(".tec--btn::attr(href)").get()

    return next_page if next_page else None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
