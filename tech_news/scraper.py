import requests
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url=url, timeout=3)
        if(response.ok):
            return response.text
        else:
            return None
    except requests.exceptions.ReadTimeout:
        return None

print(fetch("https://httpbin.org/delay/5"))


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
