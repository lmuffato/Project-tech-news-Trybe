import time
import requests
import parsel


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        requisition = requests.get(url, timeout=3)

        if requisition.status_code == 200:
            return requisition.text
        else:
            return None

    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    site_content = parsel.Selector(html_content)
    links_news = []
    for link in site_content.css("h3.tec--card__title"):
        new_link = link.css("a.tec--card__title__link::attr(href)").get()
        links_news.append(new_link)
    return links_news


# Requisito 3
def scrape_next_page_link(html_content):
    site_content = parsel.Selector(html_content)
    btn_next_page = site_content.css("a.tec--btn::attr(href)").get()

    if btn_next_page:
        return btn_next_page
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
