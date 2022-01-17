from time import sleep
import requests


# Requisito 1
def fetch(url):
    # """Seu código deve vir aqui"""
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
