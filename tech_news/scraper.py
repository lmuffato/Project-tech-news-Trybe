import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    author = selector.css("a.tec--author__info__link ::text").get()
    if author:
        return author.strip()

    author = selector.css(".tec--timestamp__item a ::text").get()
    if author:
        return author.strip()

    author = selector.css(".tec--author__info > p:first-child ::text").get()
    if author:
        return author.strip()

    return None


def getShares(content):
    selector = Selector(text=content)
    shares = selector.css(".tec--toolbar__item ::text").get()
    if shares.split(" "):
        amount = shares.split(" ")
        if amount[1] == "0" or amount[1] == "":
            return 0
        return amount[1]
    return int(shares)


def getComments(content):
    selector = Selector(text=content)
    comments = selector.css("#js-comments-btn ::attr(data-count)").get()
    return int(comments)


def getSummary(content):
    selector = Selector(text=content)
    summary = selector.css(
        ".tec--article__body > p:first_child *::text"
    ).getall()
    paragraph = "".join(summary)
    return paragraph


def getSources(content):
    selector = Selector(text=content)
    sources = selector.css(
        "#js-main > div > article > div.tec--article__body-grid > "
        "div.z--mb-16 > div > a ::text"
    ).getall()
    stripedSources = []
    counter = 0

    while counter < len(sources):
        if len(sources[counter]) == 1:
            counter += 1
        else:
            stripedSources.append(sources[counter].strip())
            counter += 1

    return stripedSources


def getCategories(content):
    selector = Selector(text=content)
    categories = selector.css("#js-categories ::text").getall()
    formatedCategories = []
    counter = 0
    while counter < len(categories):
        if categories[counter] != " ":
            formatedCategories.append(categories[counter].strip())
        counter += 1

    return formatedCategories


# Requisito 4
def scrape_noticia(html_content):
    news = {
        "url": getUrl(html_content),
        "title": getTitle(html_content),
        "timestamp": getTimestamp(html_content),
        "writer": getAuthor(html_content),
        "shares_count": getShares(html_content),
        "comments_count": getComments(html_content),
        "summary": getSummary(html_content),
        "sources": getSources(html_content),
        "categories": getCategories(html_content),
    }

    return news


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(url)
    news = scrape_novidades(html_content)
    next_page = scrape_next_page_link(html_content)
    news_right_number = []
    formated_news_to_return = []

    while len(news) < amount:
        html_content = fetch(next_page)
        other_news = scrape_novidades(html_content)

        for each_news in other_news:
            news.append(each_news)

    for each_news in news:
        if len(news_right_number) < amount:
            news_right_number.append(each_news)

    for each_news in news_right_number:
        html_content = fetch(each_news)
        news = scrape_noticia(html_content)
        formated_news_to_return.append(news)

    create_news(formated_news_to_return)
