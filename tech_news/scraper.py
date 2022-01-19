import requests
from time import sleep


# Requisito 1
def fetch(url):
    sleep(1)

    try:
        html = requests.get(url, timeout=3)

        response = {"status": html.status_code, "data": html.text}

        if response["status"] == 200:
            return response["data"]

        else:
            return None

    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""  # Pode deixar


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""  # Ok


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""  # Nem papagaio repete tanto a mesma frase


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""  # Meu código vai aonde eu quiser parceiro
