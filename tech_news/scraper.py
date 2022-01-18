import requests
import parsel
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(url, timeout=3)
        if res.status_code == 200:
            return res.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    attr = "::attr(href)"
    return selector.css(".tec--list a.tec--card__title__link"+attr).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    attr = "::attr(href)"
    return selector.css("div.tec--list.tec--list--lg > a"+attr).get()


# Requisito 4
def get_news_url(html_content):
    selector = parsel.Selector(html_content)
    links = selector.css("meta::attr(content)").getall()

    result = ""
    for link in links:
        if link.startswith("https://www.tecmundo"):
            result = link
    return result


def get_news_title(html_content):
    selector = parsel.Selector(html_content)
    title = selector.css(".tec--article__header__title::text").get()
    return title


def get_news_timestamp(html_content):
    selector = parsel.Selector(html_content)
    datetime = selector.css("#js-article-date::attr(datetime)").get()
    return datetime


def get_news_author(html_content):
    selector = parsel.Selector(html_content)
    author = selector.css(
        ".z--font-bold a ::text"
    ).get()

    if type(author) == str:
        return author.strip()

    author2 = selector.css(
        ".z--font-bold ::text"
    ).get()

    if type(author2) == str:
        return author2.strip()
    else:
        return None


def get_news_shares_count(html_content):
    selector = parsel.Selector(html_content)
    shares = selector.css(
        "#js-author-bar > nav > div:nth-child(1)::text"
    ).get()

    if type(shares) == str:
        return int(shares.strip()[0])
    return 0


def get_news_comments_count(html_content):
    selector = parsel.Selector(html_content)
    comments = selector.css("#js-comments-btn::attr(data-count)").get()
    if type(comments) == str:
        return int(comments)
    return 0


# *::text selects all descendant text nodes of the current selector context:
# fonte: https://parsel.readthedocs.io/en/latest/usage.html#using-selectors
def get_news_summary(html_content):
    selector = parsel.Selector(html_content)
    summary = selector.css(
        ".tec--article__body > p:nth-child(1) *::text"
    ).getall()
    return "".join(summary).strip()


def get_news_sources(html_content):
    selector = parsel.Selector(html_content)
    sources = selector.css(
        "div.tec--article__body-grid > div.z--mb-16 > div > a ::text"
    ).getall()

    sources_result = []
    for source in sources:
        sources_result.append(source.strip())
    return sources_result


def get_news_categories(html_content):
    selector = parsel.Selector(html_content)
    categories = selector.css(
        "#js-categories > a ::text"
    ).getall()

    categories_result = []
    for source in categories:
        categories_result.append(source.strip())
    return categories_result


def scrape_noticia(html_content):
    url = get_news_url(html_content)
    title = get_news_title(html_content)
    timestamp = get_news_timestamp(html_content)
    author = get_news_author(html_content)
    shares = get_news_shares_count(html_content)
    comments = get_news_comments_count(html_content)
    summary = get_news_summary(html_content)
    sources = get_news_sources(html_content)
    categories = get_news_categories(html_content)
    return {
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


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    news_links = []
    while len(news_links) < amount:
        html_content = fetch(url)
        news_links.extend(scrape_novidades(html_content))
        url = scrape_next_page_link(html_content)

    news = []
    for index in range(amount):
        html_news = fetch(news_links[index])
        news_data = scrape_noticia(html_news)
        news.append(news_data)

    create_news(news)
    return news
