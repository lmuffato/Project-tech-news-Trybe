import requests
from time import sleep
import parsel


# Requisito 1
def fetch(url, delay=1, timeout=3):
    try:
        sleep(delay)
        response = requests.get(url, timeout=timeout)
    except (requests.ReadTimeout, requests.HTTPError):
        return None
    else:
        if response.status_code == 200:
            return response.text


# Requisito 2
def scrape_novidades(html_content):
    links = []
    response = parsel.Selector(html_content)
    for link in response.css("h3.tec--card__title"):
        result = link.css("a.tec--card__title__link::attr(href)").get()
        links.append(result)
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    response = parsel.Selector(html_content)
    try:
        next_page = response.css("a.tec--btn--lg::attr(href)").get()
        return next_page
    except TimeoutError:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
