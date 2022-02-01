import requests
import time


# Requisito 1
def fetch(url):
    try:
        # timeout é o limite em segundos para lançar o erro timeOut
        response = requests.get(url, timeout=3)
        time.sleep(1)   # espera 1 segundo para cada resquisição
        if response.status_code != 200:
            return None   # Se não retornar status 200, retorna nenhum valor
        return response.text   # Todo o html da página
    except requests.Timeout:   # Tratamento do erro Timeout
        return None   # no caso de erro de timeOut, retorna nenhum valor


# Teste manual
print(fetch("https://www.tecmundo.com.br/novidades"))


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
