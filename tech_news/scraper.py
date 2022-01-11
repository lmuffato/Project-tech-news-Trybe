import requests
import time
import parsel


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    parselSelector = parsel.Selector(html_content)
    list = []
    for noticia in parselSelector.css("div.tec--list__item"):
        linkElement = noticia.css("a.tec--card__title__link::attr(href)").get()
        list.append(linkElement)
    return list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
