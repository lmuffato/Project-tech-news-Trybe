# Requisito 1
import time
import requests
from parsel import Selector
from tech_news.database import create_news


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            raise requests.exceptions.HTTPError
        return response.text

    except requests.ReadTimeout:
        return None
    except requests.HTTPError:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    all_news = selector.css("h3.tec--card__title a::attr(href)").getall()
    return all_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_buttons = selector.css(
        "div.tec--list.tec--list--lg > "
        "a ::attr(href)").get()
    if not next_page_buttons:
        return None
    return next_page_buttons


# AUX 4

def get_timestamp(selector):
    ts = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()

    return ts


def get_writer(selector):
    writer1 = '.z--font-bold a ::text'
    writer2 = '.z--font-bold ::text'

    writer = selector.css(writer1).get()

    if writer is None:
        writer = selector.css(writer2).get()

    return writer.strip()


def get_shares_count(selector):
    shares_count = selector.css(
        ".tec--toolbar__item::text"
        ).get()

    return int(shares_count.split()[0]) if shares_count else 0


def get_comments(selector):
    comments_count = selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get()
    if comments_count is None:
        comments_count = 0

    return int(comments_count)


def get_summary(selector):
    summary = "".join(
        selector.css(
            ".tec--article__body > p:first-child *::text"
        ).getall()
    )
    return summary


def get_sources(selector):
    arr = []
    get_sources = selector.css(".z--mb-16 a.tec--badge::text").getall()

    for source in get_sources:
        arr.append(source.strip())

    return arr


def get_categories(selector):
    arr = selector.css("#js-categories a::text").getall()
    categories = [category.strip() for category in arr]

    return categories


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css(".tec--article__header__title::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": get_timestamp(selector),
        "writer": get_writer(selector),
        "shares_count": get_shares_count(selector),
        "comments_count": get_comments(selector),
        "summary": get_summary(selector),
        "sources": get_sources(selector),
        "categories": get_categories(selector),
    }


# Requisito 5
def get_tech_news(amount):
    arr = []
    url = "https://www.tecmundo.com.br/novidades"
    while len(arr) < amount:
        html = fetch(url)
        all_news = scrape_novidades(html)
        for news in all_news:
            content = fetch(news)
            scraped_news = scrape_noticia(content)
            if len(arr) < amount:
                arr.append(scraped_news)
        url = scrape_next_page_link(html)
    create_news(arr)
    return arr
