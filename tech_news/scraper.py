from requests import get
from time import sleep

import requests


def fetch(url):
    sleep(1)
    try:
        response = get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    finally:
        if (response.status_code == 200):
            return response.content
        return None


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
