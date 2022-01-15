from time import sleep
import requests
from parsel import Selector


URL_BASE = 'https://www.tecmundo.com.br/novidades'


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        html = requests.get(url, timeout=3)
    except requests.Timeout:
        return None
    if html.status_code == 200:
        return html.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css(
        'h3.tec--card__title a.tec--card__title__link::attr(href)'
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
