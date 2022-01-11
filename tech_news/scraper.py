import requests
import time

# URL = "https://www.tecmundo.com.br/novidades"


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)

        if response.status_code != 200:
            return None
        else:
            return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# print(fetch(URL))


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
