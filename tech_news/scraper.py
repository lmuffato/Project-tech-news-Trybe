from typing import Union
import requests
import time

from requests.models import Response


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
