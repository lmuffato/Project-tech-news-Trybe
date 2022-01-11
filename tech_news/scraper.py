import requests
import time

from parsel import Selector

# path = "https://www.tecmundo.com.br/novidades"


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(url, timeout=3)
        if res.status_code == 200:
            return res.text

        return None
    except requests.Timeout:
        return None


# print(fetch(path))


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    list_urls = selector.css("h3.tec--card__title a::attr(href)").getall()

    return list_urls


# html = fetch(path)
# print(scrape_novidades(html))


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    pass


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    pass


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    pass
