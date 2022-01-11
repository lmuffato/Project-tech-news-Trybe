import time
import requests
import parsel


# Requisito 1
def fetch(url):
    try:
        # README: "utilizar time.sleep(1) antes de cada requisição"
        time.sleep(1)
        requisicao = requests.get(url, timeout=3)

        if requisicao.status_code == 200:
            return requisicao.text
        else:
            return None

    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    conteudo = parsel.Selector(html_content)
    links = []

    for link in conteudo.css("h3.tec--card__title"):
        noticia = link.css("a.tec--card__title__link::attr(href)").get()
        links.append(noticia)

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
