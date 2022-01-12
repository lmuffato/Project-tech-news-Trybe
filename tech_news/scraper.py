import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    urls = []
    for div in selector.css(".tec--card__info"):
        url = div.css("h3 a::attr(href)").get()
        if url is not None:
            urls.append(url)
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next = selector.css(".tec--btn--primary::attr(href)").get()
    return next


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()

    title = selector.css("#js-article-title::text").get()

    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()

    writer = selector.css(".z--font-bold *::text").get()
    if writer:
        writer = writer.strip()

    shares = selector.css(".tec--toolbar__item::text").get()
    if shares:
        shares = int(shares.split()[0])
    else:
        shares = 0

    comments = selector.css("#js-comments-btn::attr(data-count)").get()

    summary = "".join(
        selector.css(".tec--article__body p:nth-child(1) *::text").getall()
    )

    categories = [
        category.strip()
        for category in selector.css("#js-categories a::text").getall()
    ]

    sources = [
        source.strip()
        for source in selector.css(
            ".z--mb-16 .tec--badge::text"
        ).getall()
    ]

    data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares,
        "comments_count": int(comments),
        "summary": summary,
        "categories": categories,
        "sources": sources,
    }

    return data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
