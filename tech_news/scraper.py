from requests import get
from time import sleep
from bs4 import BeautifulSoup
import requests


def fetch(url):
    sleep(1)
    response = None
    try:
        response = get(url, timeout=3)
        if (response.status_code == 200):
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    returnList = []
    readed = BeautifulSoup(html_content)
    div = readed.find('div', attrs={'class': "tec--list--lg"})
    if div is None:
        return returnList
    test = div.find_all_next('a', attrs={'class': "tec--card__thumb__link"})
    for a in test:
        returnList.append(a.get('href'))
    return returnList


# Requisito 3
def scrape_next_page_link(html_content):
    readed = BeautifulSoup(html_content)
    a = readed.find('a', 'tec--btn')
    if a is None:
        return None
    link = a.get('href')
    return link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
