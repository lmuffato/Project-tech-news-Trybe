import requests
from parsel import Selector
import time
from tech_news.database import create_news


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(3)

        if response.status_code != 200:
            return None

        return response.text

    except requests.Timeout:
        return None


def get_writer(selector):
    writer = selector.css(
        '.tec--author__info__link::text').get()
    if not writer:
        writer = selector.css(
            '.tec--timestamp__item.z--font-bold a::text').get()
    if not writer:
        writer = selector.css(
            '.tec--author__info p::text').get()
    return writer.strip() if writer else None


def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    get_shares_count = selector.css(
        "#js-author-bar > nav > div:nth-child(1)::text"
    ).re_first(r"\d+")
    share_count = int(get_shares_count) if get_shares_count else 0

    comments_count = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )
    get_summary = selector.css(
        ".tec--article__body > p:nth-of-type(1) *::text"
    ).getall()

    summary = "".join(get_summary)
    get_sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    sources = [source.strip() for source in get_sources]
    get_categories = selector.css("#js-categories > a *::text").getall()
    categories = [category.strip() for category in get_categories]

    allNews = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": get_writer(selector),
        "shares_count": share_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }

    return allNews


def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    newsSection = selector.css(
        '.tec--list a.tec--card__title__link::attr(href)'
    ).getall()

    return newsSection


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    nextPage = selector.css('.tec--list > a::attr(href)').get() or None

    return nextPage


def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    allNews = []
    while len(allNews) < amount:
        request = fetch(url)
        newsList = scrape_novidades(request)
        for item in newsList:
            newsURL = fetch(item)
            allNews.append(scrape_noticia(newsURL))
            if len(allNews) == amount:
                create_news(allNews)
                return allNews
        url = scrape_next_page_link(request)
