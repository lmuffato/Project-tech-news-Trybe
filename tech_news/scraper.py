from typing import Union
from requests.models import Response

import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url: str) -> Union[Response, None]:
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if(response.status_code != 200):
            return None
        return response.text
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content: str) -> list:
    selector = Selector(text=html_content)
    # É preciso resgatar os links via <h3>
    # ao invés de direto pelo <a> para retornar quantidade correta
    news_links = [a.attrib['href'] for a in selector.css(
        'h3.tec--card__title').css('a')]
    return news_links


html = fetch('https://www.tecmundo.com.br/novidades')
print(len(scrape_novidades(html)))


# Requisito 3
def scrape_next_page_link(html_content: str) -> list:
    selector = Selector(text=html_content)
    next_page_link_href = selector.css('a.tec--btn::attr(href)').get()
    return next_page_link_href


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
