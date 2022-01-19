import requests
import time
from parsel import Selector
from .database import create_news


# Requisito 1
def fetch(url):
    try:
        res = requests.get(url)
        time.sleep(1)
        if res.status_code == 200:
            return res.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    arr = []
    if len(arr) == 0:
        return selector.css(
            ".tec--list .tec--card__title__link::attr(href)"
            ).getall()
    else:
        return arr


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next = selector.css(".tec--btn::attr(href)").get()
    if next != "":
        return next
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    arr = []
    html_content = fetch("https://www.tecmundo.com.br/novidades")
    arr.extend(scrape_novidades(html_content))
    while len(arr) < amount:
        next = scrape_next_page_link(html_content)
        page = fetch(next)
        arr.extend(scrape_novidades(page))

    news = []
    for item in arr[:amount]:
        html_content = fetch(item)
        news.append(scrape_noticia(html_content))

    create_news(news)
    return news
