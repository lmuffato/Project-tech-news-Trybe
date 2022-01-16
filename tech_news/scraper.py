import requests
import time
import parsel


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(url, timeout=3)
        if res.status_code == 200:
            return res.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    list = []
    for news in selector.css("h3.tec--card__title a::attr(href)").getall():
        list.append(news)
    return list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    btn = selector.css("a.tec--btn::attr(href)").get()
    if btn:
        return btn
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
