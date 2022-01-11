import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None

# print(fetch("http://quotes.toscrape.com/page/1"))


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links_list = []
    for news_link in selector.css("h3.tec--card__title"):
        link = news_link.css("a.tec--card__title__link::attr(href)").get()
        links_list.append(link)
    return links_list


# Documentação Parsel:
# https://parsel.readthedocs.io/en/latest/usage.html


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css("a.tec--btn::attr(href)").get()
    if next_page_link:
        return next_page_link
    else:
        return None


# test = fetch("https://www.tecmundo.com.br/novidades")
# print(scrape_next_page_link(test))


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
