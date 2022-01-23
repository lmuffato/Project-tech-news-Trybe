import time
import requests
from parsel import Selector
from .database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link = selector.css("a.tec--btn::attr(href)").getall()

    return link[0] if link else None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".z--font-bold *::text").get()
    writer = writer.strip() if writer else None
    shares_count = selector.css(".tec--toolbar__item::text").get()
    shares_count = shares_count.strip().split(" ")[0] if shares_count else 0
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    comments_count = comments_count if comments_count else 0
    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    summary = "".join(summary)
    sources = [
        source.strip()
        for source in selector.css(".z--mb-16 div a::text").getall()
    ]
    categories = [
        category.strip()
        for category in selector.css("#js-categories a::text").getall()
    ]
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
# https://github.com/tryber/sd-010-a-tech-news/pull/92/commits/c3783b51a7c7dc97c9b23de5a96c9b1d44825723

def get_tech_news(amount):
    url = fetch("https://www.tecmundo.com.br/novidades")
    links = scrape_novidades(url)

    while len(links) < amount:
        more_pages = scrape_next_page_link(url)
        next_page = fetch(more_pages)
        links.extend(scrape_novidades(next_page))

    notes = [scrape_noticia(fetch(element)) for element in links[:amount]]

    create_news(notes)
    return notes
