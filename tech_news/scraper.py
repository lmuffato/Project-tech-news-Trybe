import requests
import time
import re
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    list = []
    selector = Selector(text=html_content)

    for url in selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall():
        list.append(url)

    return list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css(
        "a.tec--btn.tec--btn--lg.tec--btn-" +
        "-primary.z--mx-auto.z--mt-48::attr(href)"
    ).get()

    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css(
        "head meta[property='og:url']::attr(content)"
    ).get()

    title = selector.css(
        "article.tec--article h1#js-article-title::text"
    ).get()

    date = selector.css(
        "article.tec--article time#js-article-date::attr(datetime)"
    ).get()

    author = selector.css(
        ".z--font-bold ::text"
    ).get()

    if not author:
        newswritter = None
    else:
        newswritter = author.strip()

    share = selector.css(
        "article.tec--article div.tec--toolbar__item::text"
    ).get()

    if not share:
        share_count = 0
    else:
        share_count = int(re.findall('[0-9]+', share)[0])

    synopsis = selector.css(
        "article.tec--article div.tec--article__body p:first_child *::text"
    ).getall()

    news_synopsis = "".join(synopsis).strip()

    sources = selector.css(
        "article.tec--article div.z--mb-16 a.tec--badge::text"
    ).getall()

    news_source = [source.strip() for source in sources]

    categorization = selector.css(
        "article.tec--article div#js-categories a.tec--badge::text"
    ).getall()

    categories = [category.strip() for category in categorization]

    tecmundo_news = dict({
        "url": url,
        "title": title,
        "timestamp": date,
        "writer": newswritter,
        "shares_count": share_count,
        "comments_count": 0,
        "summary": news_synopsis,
        "sources": news_source,
        "categories": categories,
    })

    return tecmundo_news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
