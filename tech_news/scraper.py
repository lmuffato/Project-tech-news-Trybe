import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.HTTPError as err:
        print(err)
        response = None
    finally:
        if response.status_code == 200:
            return response
        else:
            return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content.text)
    news_item = selector.css('.tec--list__item').getall()
    news_url = []
    for item in news_item:
        url = item.css('article figure a::href')
        news_url.append(url)
    return news_url


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
