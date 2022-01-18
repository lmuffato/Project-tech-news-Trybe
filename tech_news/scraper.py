# Requisito 1
import time
import requests


def fetch(url):
    try:
        time.sleep(1)
        fetch_html = requests.get(url, timeout=3)

        if fetch_html.status_code == 200:
            return fetch_html.text
        else:
            return None

    except requests.Timeout:
        return None


# REQUISITO 2
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
