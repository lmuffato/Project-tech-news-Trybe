from parsel import Selector
from tech_news.database import create_news
import requests
import time


# Requisito 1
def fetch(url):
    try:
        delay = 1
        timeout = 3

        time.sleep(delay)

        response = requests.get(url, timeout=timeout)

        if response.status_code != 200:
            raise requests.exceptions.HTTPError

        return response.text
    except (requests.ReadTimeout, requests.exceptions.HTTPError):
        return None


# Requisito 2
def scrape_novidades(html_content, amount=-1):
    selector = Selector(text=html_content)
    news = []
    css = {
        "item-info": ".tec--list__item .tec--card__info",
        "title-link": ".tec--card__title .tec--card__title__link",
        "extra": "::attr(href)",
    }

    css_new = f"{css['item-info']} {css['title-link']}{css['extra']}"

    for new in selector.css(css_new):
        news.append(new.get())

    if amount == -1:
        return news

    return getManyNews(news=news, amount=amount)


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    css_link = ".tec--page-filters ~ .tec--list > a::attr(href)"

    next_page_link = selector.css(css_link).get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    css_new = {
        "url": "head link[rel=canonical]::attr(href)",
        "title": ".tec--article__header__title::text",
        "timestamp": "#js-article-date::attr(datetime)",
        "writer": ".z--font-bold *::text",
        "shares_count": ".tec--toolbar__item::text",
        "comments_count": "#js-comments-btn::attr(data-count)",
        "summary": ".tec--article__body > p:first-child *::text",
        "sources": ".z--mb-16 .tec--badge::text",
        "categories": "#js-categories > a::text",
    }

    return {
        "url": selector.css(css_new["url"]).get(),
        "title": selector.css(css_new["title"]).get(),
        "timestamp": selector.css(css_new["timestamp"]).get(),
        "writer": parse_writer(selector.css(css_new["writer"]).get()),
        "shares_count": parse_shares_count(
            selector.css(css_new["shares_count"])
        ),
        "comments_count": parse_comments_count(
            selector.css(css_new["comments_count"]).get()
        ),
        "summary": "".join(selector.css(css_new["summary"]).getall()),
        "sources": parse_sourcers(selector.css(css_new["sources"]).getall()),
        "categories": parse_categories(
            selector.css(css_new["categories"]).getall()
        ),
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(url)
    html_news = scrape_novidades(html_content, amount)
    news = [scrape_noticia(fetch(html_new)) for html_new in html_news]
    create_news(news)
    return news


# Helpers
def getManyNews(news, amount):
    return news[0:amount]


def parse_url(links):
    url = ""

    for link in links:
        infos = link.split(" ")
        rel = infos[1]

        if "canonical" in rel:
            href = infos[2].split('"')[1]
            url = href

    return url


def parse_shares_count(count):
    return int(count.get().split(" ")[1]) if count else 0


def parse_comments_count(count):
    return int(count) if count else 0


def parse_writer(writer):
    return writer.strip() if writer else writer


def parse_sourcers(sources):
    return [source.strip() for source in sources]


def parse_categories(categories):
    return [categorie.strip() for categorie in categories]
