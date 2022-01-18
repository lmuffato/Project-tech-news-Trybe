import time
import requests
import parsel


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        fetch_html = requests.get(url, timeout=3)

        if fetch_html.status_code == 200:
            return fetch_html.text
        else:
            return None

    except requests.Timeout:
        return None


# REQUISITO 2
def scrape_novidades(html_content):
    code = parsel.Selector(html_content)
    links = []

    for element in code.css("h3.tec--card__title"):
        fetch_link = element.css("a.tec--card__title__link::attr(href)").get()
        links.append(fetch_link)

    return links


# REQUISITO 3
def scrape_next_page_link(html_content):
    code = parsel.Selector(html_content)
    button = code.css("a.tec--btn::attr(href)").get()

    if button:
        return button
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
