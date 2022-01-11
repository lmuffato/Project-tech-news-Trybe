from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        return requests.get(url, timeout=3).text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls = selector.css('.tec--card__title__link::attr(href)').getall()
    if(urls):
        return urls
    return []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    btn_next_page = selector.css('.tec--btn--primary::attr(href)').get()
    if(btn_next_page):
        return btn_next_page
    return None


# Requisito 4
def scrape_noticia(html_content):
    pass   


# Requisito 5
def get_tech_news(amount):
    pass
    """Seu código deve vir aqui"""
