import time
import requests
import parsel


def fetch(url):
    try:
        time.sleep(1)
        request = requests.get(url, timeout=3)
        if request.status_code == 200:
            return request.text
        else:
            return None
    except requests.Timeout:
        return None


def scrape_novidades(html_content):
    content = parsel.Selector(html_content)
    list_url = []

    for url in content.css("h3.tec--card__title"):
        reports = url.css("a.tec--card__title__link::attr(href)").get()
        list_url.append(reports)

    return list_url


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
