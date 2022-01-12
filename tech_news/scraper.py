import time
import requests
import parsel


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    listLinks = []

    for link in selector.css("h3.tec--card__title"):
        noticia = link.css("a.tec--card__title__link::attr(href)").get()
        listLinks.append(noticia)

    return listLinks


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
