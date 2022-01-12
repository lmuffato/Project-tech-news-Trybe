import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None
    if response.status_code != 200:
        return None

    return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    links_list = []
    for news_link in selector.css("h3.tec--card__title"):
        link = news_link.css("a.tec--card__title__link::attr(href)").get()
        links_list.append(link)
    return links_list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    link_button_selector = ".tec--list .tec--btn.tec--btn--primary::attr(href)"
    next_page_button_link = selector.css(link_button_selector).get()
    if not next_page_button_link:
        return None
    else:
        return next_page_button_link
    

# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
