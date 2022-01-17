from time import sleep
import requests
from parsel import Selector
URL_BASE = 'https://www.tecmundo.com.br/novidades'


# Requisito 1
def fetch(url):
    # """Seu código deve vir aqui"""
    sleep(1)
    # Garante o intervalo de 1 segundo entre cada requisição.
    try:
        html = requests.get(url, timeout=3)
        # Permite http requests usando python
    except requests.Timeout:
        return None
    if html.status_code == 200:
        return html.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    # """Seu código deve vir aqui"""
    selector = Selector(html_content)
    return selector.css(
        'main .tec--card__title__link::attr(href)'
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
