import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    if html_content == "":
        return []
    selector = Selector(text=html_content)
    list = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 > div.tec--list"
        ".tec--list--lg article > div > h3 > a ::attr(href)"
    ).getall()
    return list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 > "
        "div.tec--list.tec--list--lg > a ::attr(href)"
    ).get()
    return link


def getUrl(content):
    selector = Selector(text=content)
    url = selector.css("head > link[rel=canonical] ::attr(href)").get()
    return url


def getTitle(content):
    selector = Selector(text=content)
    title = selector.css("#js-article-title ::text").get()
    return title


def getTimestamp(content):
    selector = Selector(text=content)
    timestamp = selector.css("#js-article-date ::attr(datetime)").get()
    return timestamp


def getAuthor(content):
    selector = Selector(text=content)
    author = selector.css(".tec--author__info__link ::text").get()
    return author


def getShares(content):
    selector = Selector(text=content)
    shares = selector.css(".tec--toolbar__item ::text").get()
    return shares


def getComments(content):
    selector = Selector(text=content)
    comments = selector.css("#js-comments-btn ::attr(data-count)").get()
    return comments


def getSummary(content):
    selector = Selector(text=content)
    summary = selector.css(
        ".tec--article__body > p:first_child *::text"
    ).getall()
    return summary


def getSources(content):
    selector = Selector(text=content)
    sources = selector.css(".tec--badge ::text").getall()
    return sources


def getCategories(content):
    selector = Selector(text=content)
    categories = selector.css("#js-categories ::text").getall()
    return categories


# Requisito 4
def scrape_noticia(html_content):
    url = getUrl(html_content)
    title = getTitle(html_content)
    timestamp = getTimestamp(html_content)
    author = getAuthor(html_content)
    shares = getShares(html_content)
    comments = getComments(html_content)
    summary = getSummary(html_content)
    sources = getSources(html_content)
    categories = getCategories(html_content)

    news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": author,
        "shares_count": shares,
        "comments_count": comments,
        "summary": summary,
        "sources": sources,
        "categories": categories
    }

    print(news)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
