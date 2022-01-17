import requests
import time
import parsel


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    novidades = parsel.Selector(html_content)
    return novidades.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    conteudoHtml = parsel.Selector(html_content)
    url = conteudoHtml.css("a.tec--btn::attr(href)").get()
    if url:
        return url
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
