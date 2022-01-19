import time
import requests
import parsel


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        html = requests.get(url, timeout=3)

        if html.status_code == 200:
            return html.text
        return None

    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)

    links = [
        cardTitle.css("a.tec--card__title__link::attr(href)").get()
        for cardTitle in selector.css("h3.tec--card__title")
    ]
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    nextLinkPage = selector.css("a.tec--btn::attr(href)").get()

    if nextLinkPage:
        return nextLinkPage
    return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
