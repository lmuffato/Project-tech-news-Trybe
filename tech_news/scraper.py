import requests
import time
from parsel import Selector
from tech_news.database import create_news

URL_NEXT_PAGE_SELECTOR = ".tec--list a.tec--btn::attr(href)"

AUTHOR_SELECTOR = ".z--font-bold ::text"

URL_NEWS_SELECTOR = "head > link[rel=canonical]::attr(href)"

TITLE_SELECTOR = "#js-article-title::text"

TIMESTAMP_SELECTOR = "#js-article-date::attr(datetime)"

SOURCES_SELECTOR = ".z--mb-16 .tec--badge::text"

CATEGORIES_SELECTOR = "#js-categories a::text"

SHARES_COUNT_SELECTOR = "#js-author-bar > nav > div:nth-child(1)::text"

COMMENTS_COUNT_SELECTOR = "#js-comments-btn::attr(data-count)"

SUMMARY_SELECTOR = ".tec--article__body > p:first_child *::text"

# Requisito 1


def fetch(url):
    try:
        time.sleep(1)
        data = requests.get(url, timeout=3)
        data.raise_for_status()
        return data.text
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    url_list = list()

    for url in selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall():
        url_list.append(url)

    return url_list

# Requisito 3


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    url = selector.css(URL_NEXT_PAGE_SELECTOR).get()
    return url


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = selector.css(URL_NEWS_SELECTOR).get()

    title = selector.css(TITLE_SELECTOR).get()

    timestamp = selector.css(TIMESTAMP_SELECTOR).get()

    writer = selector.css(AUTHOR_SELECTOR).get()

    if writer:
        writer = writer.strip()
    else:
        writer = None

    sources = [
        source.strip() for source in selector.css(SOURCES_SELECTOR).getall()
        ]

    categories = [
        category.strip() for category in
        selector.css(CATEGORIES_SELECTOR).getall()
        ]

    shares_count = selector.css(SHARES_COUNT_SELECTOR).get()

    if shares_count:
        shares_count = shares_count.split()[0]
    else:
        shares_count = 0

    comments_count = selector.css(COMMENTS_COUNT_SELECTOR).get()

    summary = "".join(selector.css(SUMMARY_SELECTOR).getall())

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "sources": sources,
        "categories": categories,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary
    }
# Requisito 5


def get_tech_news(amount):
    news = []
    url = "https://www.tecmundo.com.br/novidades"

    while len(news) < amount:
        page = fetch(url)

        url_news_list = scrape_novidades(page)

        for url_news in url_news_list:
            if len(news) == amount:
                break

            news_details_page = fetch(url_news)
            data_extracted_from_news = scrape_noticia(news_details_page)
            news.append(data_extracted_from_news)

        if len(news) != amount:
            url = scrape_next_page_link(page)

    create_news(news)

    return news
