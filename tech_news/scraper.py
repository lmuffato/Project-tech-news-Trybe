from parsel import Selector
import requests
from time import sleep
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        response = ""
    finally:
        if not response or response.status_code != 200:
            return None
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    URLS = selector.css(
        ".tec--list .tec--card__title__link::attr(href)"
    ).getall()
    return URLS if URLS else []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(".tec--btn::attr(href)").get()
    return next_page_link if next_page_link else None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    news_url = selector.css("head link[rel=canonical]::attr(href)").get()

    news_title = selector.css(".tec--article__header__title::text").get()

    news_timestamp = selector.css("#js-article-date::attr(datetime)").get()

    author = selector.css(".z--font-bold *::text").get()
    news_author = author.strip() if author else None

    shares_count = selector.css(".tec--toolbar__item::text").get()
    news_shares_count = (
        shares_count.strip().split(" ")[0] if shares_count else 0
    )

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    news_comments_count = comments_count if comments_count else 0

    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    news_summary = "".join(summary)

    news_sources = []
    for source in selector.css(".z--mb-16 div a::text").getall():
        news_sources.append(source.strip())

    news_categories = []
    for category in selector.css("#js-categories a::text").getall():
        news_categories.append(category.strip())

    return {
        "url": news_url,
        "title": news_title,
        "timestamp": news_timestamp,
        "writer": news_author,
        "shares_count": int(news_shares_count),
        "comments_count": int(news_comments_count),
        "summary": news_summary,
        "sources": news_sources,
        "categories": news_categories,
    }


# Requisito 5
def get_tech_news(amount):
    initial_page = "https://www.tecmundo.com.br/novidades"
    page = fetch(initial_page)
    URLS = scrape_novidades(page)
    news = []
    # while page_link:
    # counter = 0
    while len(URLS) < amount:
        next_page_link = scrape_next_page_link(page)
        page = fetch(next_page_link)
        URLS += scrape_novidades(page)

    for url in URLS[:amount]:
        noticia = fetch(url)
        news.append(scrape_noticia(noticia))

    create_news(news)

    return news
