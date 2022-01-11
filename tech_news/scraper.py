import requests
import time

from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if(response.status_code == 200):
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    href_news = selector.css("h3.tec--card__title a::attr(href)").getall()
    list_href_news = []
    for href in href_news:
        list_href_news.append(href)
    return list_href_news


# html = fetch("https://www.tecmundo.com.br/novidades")
# print(scrape_novidades(html))


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_url = selector.css(
        "div.tec--list.tec--list--lg a.tec--btn.tec--btn--lg::attr(href)"
    ).get()
    return next_page_url


# html = fetch("https://www.tecmundo.com.br/novidades")
# print(scrape_next_page_link(html))


# Requisito 4
def scrape_noticia(html_content):
    pass


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
