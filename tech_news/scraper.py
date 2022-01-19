import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
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
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    list_href = selector.css(
        ".tec--list .tec--card .tec--card__info \
            .tec--card__title a[href*=htm]::attr(href)"
    ).getall()
    return list_href


# html = fetch("https://www.tecmundo.com.br/novidades")
# # print(html)
# scrape_novidades(html)


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    list_href = selector.css(".tec--list a[href*=page]::attr(href)").get()
    return list_href


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
