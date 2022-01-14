import requests
import time
import parsel
# import math


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    links = []
    for new in selector.css("div.tec--list__item"):
        link = new.css("a.tec--card__title__link::attr(href)").get()
        links.append(
            link,
        )
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    try:
        next_page_link = selector.css("a.tec--btn--lg::attr(href)").get()
        return next_page_link
    except requests.Timeout:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
