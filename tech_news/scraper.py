import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        res = requests.get(url, timeout=2)
        time.sleep(1)
        if res.status_code == 200:
            return res.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    urls_arr = []
    selector = Selector(html_content)
    cards = selector.css("div .tec--list__item")
    for card in cards:
        url = card.xpath(".//article/figure/a/@href").get()
        print(url)
        urls_arr.append(url)
    return urls_arr


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
