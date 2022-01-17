from time import sleep
import requests
from parsel import Selector
from .scraper_news import get_url, get_title, get_timestamp, get_summary
from .scraper_news import get_writer, get_shares_count, get_comments_count
from .scraper_news import get_sources, get_categories


URL_BASE = 'https://www.tecmundo.com.br/novidades'


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        html = requests.get(url, timeout=3)
    except requests.Timeout:
        return None
    if html.status_code == 200:
        return html.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css(
        'h3.tec--card__title a.tec--card__title__link::attr(href)'
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css('a.tec--btn::attr(href)').get()
    if next_page:
        return next_page
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    news = {
        'url': get_url(selector),
        'title': get_title(selector),
        'timestamp': get_timestamp(selector),
        'writer': get_writer(selector),
        'shares_count': get_shares_count(selector),
        'comments_count': get_comments_count(selector),
        'summary': get_summary(selector),
        'sources': get_sources(selector),
        'categories': get_categories(selector),
    }

    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
