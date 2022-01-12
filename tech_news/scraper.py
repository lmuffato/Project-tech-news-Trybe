import requests
import time
import parsel

# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)  
    except requests.ReadTimeout:
        return None
    if response.status_code and response.status_code == 200:
        return response.text 
    return None

# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    return selector.css(".tec--list__item  .tec--card__title__link::attr(href)").getall()

# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    return selector.css(".tec--btn::attr(href)").get()

# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
