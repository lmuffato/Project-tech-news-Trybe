import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    links = selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
        ).getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css(".tec--btn::attr(href)").get()
    return next_page_url if next_page_url else None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css(
        "#js-article-date::attr(datetime)"
        ).get()
    author = selector.css(".z--font-bold *::text").get()
    writer = author.strip() if author else None
    shares = selector.css(".tec--toolbar__item::text").get()
    shares_count = (
        shares.strip().split(" ")[0] if shares else 0
    )
    comments = selector.css("#js-comments-btn::attr(data-count)").get()
    comments_count = comments if comments else 0
    summary = selector.css(
        ".tec--article__body p:first-child *::text"
        ).getall()
    response_summary = "".join(summary)
    response_sources = []
    for source in selector.css(".z--mb-16 div a::text").getall():
        response_sources.append(source.strip())
    response_categories = []
    for category in selector.css("#js-categories a::text").getall():
        response_categories.append(category.strip())

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": response_summary,
        "sources": response_sources,
        "categories": response_categories,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
