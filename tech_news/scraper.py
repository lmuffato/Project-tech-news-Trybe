import requests  # permite realizar requisições http
import time  # acesso a horário e conversões


# Requisito 1
def fetch(url):  # função fetch recebe uma url
    try:
        # requisição http definindo timeout de 3seg
        response = requests.get(url, timeout=3)
        time.sleep(1)  # rate limite 1 segundo
        if response.status_code != 200:  # retorna um number
            return None  # retorna none se status_code for diferente de 200
        return response.text  # retorna conteúdo de texto caso status seja 200
    except requests.Timeout:  # caso não receba resposta no time especificado..
        return None  # retorna none


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
