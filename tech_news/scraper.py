import requests
import time
import parsel
# Requisito 1


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text
    

# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    links = selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
        ).getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
