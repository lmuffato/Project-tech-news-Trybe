# requests: permite realizar requisições http
import requests
# tine: acesso a horário e conversões
import time
# parsel: lib para extrair dados de html e xml...
# usando seletores xpath e css podendo ser combinados com regex
# https://pythonrepo.com/repo/scrapy-parsel-python-web-crawling
from parsel import Selector


# Requisito 1
# função fetch recebe uma url
def fetch(url):
    try:
        # requisição http definindo timeout de 3seg
        response = requests.get(url, timeout=3)
        # rate limite 1 segundo
        time.sleep(1)
        # status_code: retorna um number
        if response.status_code != 200:
            # retorna none se status_code for diferente de 200
            return None
        # retorna conteúdo de texto caso status seja 200
        return response.text
    # caso não receba resposta no time especificado retorna none
    except requests.Timeout:
        return None


# Requisito 2
# recebe url
def scrape_novidades(html_content):
    #  guarda o conteúdo de texto
    data = Selector(text=html_content)
    #  a::attr(href) captura somente o valor contido no texto do seletor 'a'
    list = data.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()
    #  retorna uma lista e se nao encontrar nenhuma URL retorna uma lista vazia
    if (list):
        return list
    else:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
