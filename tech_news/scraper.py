import requests
import time

# Requisito 1
limit_time = 3
status_ok = 200


def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        res = requests.get(url, timeout=limit_time)
        if (res.status_code == status_ok):
            return res.text
        return None
    except requests.Timeout:
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
