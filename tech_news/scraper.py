import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):

    try:
        res = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if res.status_code == 200:
        return res.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    res = Selector(html_content)
    res_links = res.css(
        "div.tec--list__item > article > div > h3 > a::attr(href)"
    ).getall()
    return res_links


# Requisito 3
def scrape_next_page_link(html_content):

    res = Selector(html_content)
    res_next_page = res.css(
        "div.z--col.z--w-2-3 > div.tec--list.tec--list--lg > a ::attr(href)"
    ).get()
    return res_next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
