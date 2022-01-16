from ratelimit import limits, sleep_and_retry
from parsel import Selector
from tech_news.database import create_news

import requests

# Requisito 1


@sleep_and_retry
@limits(calls=1, period=1)
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    data = Selector(html_content)
    return data.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css("div.tec--list a.tec--btn::attr(href)").get()

    if next_page_link:
        return next_page_link
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    author = selector.css(".z--font-bold *::text").get().strip()
    shares_count = selector.css(".tec--toolbar__item::text").get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary_selector = ".tec--article__body > p:first-child *::text"

    # https://www.w3schools.com/python/ref_string_strip.asp
    summary = "".join(selector.css(summary_selector).getall()).strip()

    # https://www.geeksforgeeks.org/scrapy-selectors/
    selected_sources = ".z--mb-16 a.tec--badge::text"
    sources_list = selector.css(selected_sources).getall()
    sources = [source.strip() for source in sources_list]
    selected_categories = "#js-categories a::text"
    categories_list = selector.css(selected_categories).getall()
    categories = [category.strip() for category in categories_list]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": author if author else None,
        "shares_count": int(shares_count.split()[0]) if shares_count else 0,
        "comments_count": int(comments_count) if comments_count else 0,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
def get_tech_news(amount):
    content = fetch("https://www.tecmundo.com.br/novidades")
    url = []
    news_links = []
    url.extend(scrape_novidades(content))

    while len(url) < amount:
        next_page_link = scrape_next_page_link(content)
        next_page = fetch(next_page_link)
        url.extend(scrape_novidades(next_page))

    for i in url[:amount]:
        news = fetch(i)
        news_links.append(scrape_noticia(news))

    create_news(news_links)
    return news_links
