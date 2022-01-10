import requests
from time import sleep


# Requisito 1
def fetch(url, delay=1, timeout=3):
    try:
        sleep(delay)
        response = requests.get(url)
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
