import requests
import time
from parsel import Selector
from .database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None

    if response.status_code != 200:
        return None

    return response.text


# Requisito 2
def scrape_novidades(html_content):
    content = Selector(html_content)
    # Fonte: https://parsel.readthedocs.io/en/latest/usage.html
    news_list = content.css("h3.tec--card__title a::attr(href)").getall()
    return news_list


# Requisito 3
def scrape_next_page_link(html_content):
    content = Selector(html_content)
    next_page_selector = content.css("a.tec--btn::attr(href)").get()
    return next_page_selector


# Requisito 4
def __get_writer(content):
    selectors = [
        ".tec--author__info__link::text",
        ".tec--timestamp a::text",
        "#js-author-bar > div p::text",
    ]
    for selector in selectors:
        result = content.css(selector).get()
        if result is not None:
            return result.strip()
    return None


def __get_comments_count(content):
    comments = 0
    try:
        comments = int(
            # Fonte:https://docs.python.org/pt-br/3/library/re.html
            # https://www.youtube.com/watch?v=wBI0yv2FG6U
            # https://parsel.readthedocs.io/en/latest/usage.html 
            # (Using selectors with regular expressions)
            content.css("#js-comments-btn::text").re(r"\d+")[0]
        )
    except IndexError:
        return 0
    finally:
        if comments is not None:
            return comments
    return 0


def scrape_noticia(html_content):
    content = Selector(html_content)

    url = content.css("head > link[rel=canonical]::attr(href)").get()
    title = content.css(".tec--article__header__title::text").get()
    timestamp = content.css("time::attr(datetime)").get()
    writer = __get_writer(content)
    shares_count = content.css(".tec--toolbar__item::text").get()
    comments_count = __get_comments_count(content)
    summary = "".join(content.css(
        ".tec--article__body > p:nth-child(1) *::text"
    ).getall())
    sources = [
        source.strip()
        for source in content.css(".z--mb-16 > div > a::text").getall()
        if source not in [" ", "Fontes"]
    ]

    categories = [
        category.strip()
        for category in content.css("#js-categories *::text").getall()
        if category != " "
    ]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count.split()[0]) if shares_count else 0,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
def add_news(news):
    news_list = []
    for url in news:
        content = fetch(url)
        new = scrape_noticia(content)
        news_list.append(new)
    create_news(news_list)
    return news_list


def get_tech_news(amount):
    pagination = ""
    url = "https://www.tecmundo.com.br/novidades"
    content = fetch(url + pagination)
    last_news = scrape_novidades(content)

    while len(last_news) < amount:
        pagination = (scrape_next_page_link(content)).split("/novidades")[1]
        content = fetch(url + pagination)
        last_news.extend(scrape_novidades(content))
    news = last_news[:amount]
    return add_news(news)
