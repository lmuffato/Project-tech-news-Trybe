# Requisito 1
import time
import requests
from parsel import Selector


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


######################################################################################
# AUX

def get_writer(selector):
    writer1 = '.z--font-bold a ::text'
    writer2 = '.z--font-bold ::text'

    writer = selector.css(writer1).get()

    if writer is None:
        writer = selector.css(writer2).get()

    return writer.strip()


def get_shares_count(selector):
    shares_count = selector.css(
        "#js-author-bar > nav >"
        "div:nth-child(1)::text"
        ).get()

    if shares_count is None or not ('Compartilharam'):
        shares_count = 0

    return shares_count


def get_comments(selector):
    comments_count = selector.css(
        "#button#js-comments-btn"
        "::attr(data-count)"
        ).get()
    if comments_count is None:
        comments_count = 0

    return int(comments_count)


def get_summary(selector):
    summary = "".join(
        selector.css(
            "div.tec--article__body > p:first-child *::text"
        ).getall()
    )
    return summary


def get_sources(selector):
    arr = []
    get_sources = selector.css("div.z--mb-16 a::text").getall()

    for source in get_sources:
        arr.append(source.strip())

    return arr


def get_categories(selector):
    arr = []
    categories = selector.css(
            "#js-categories ::text"
            ).getall()

    for cat in categories:
        arr.append(cat.strip())
    return arr


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("link[rel=canonical] ::attr(href)").get()
    title = selector.css("#js-article-title ::text").get()
    timestamp = selector.css("#js-article-date > strong ::text").get()
    writer = get_writer(selector)

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": get_shares_count(selector),
        "comments_count": get_comments(selector),
        "summary": get_summary(selector),
        "sources": get_sources(selector),
        "categories": get_categories(selector),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
