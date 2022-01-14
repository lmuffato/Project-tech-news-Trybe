import requests
import time
from parsel import Selector
import re
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        my_request = requests.get(url, timeout=3)
        if my_request.status_code not in [requests.codes.ok]:
            return None
        return my_request.text
    except requests.Timeout:
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_selector = ".tec--list .tec--card__title__link::attr(href)"
    return selector.css(news_selector).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--list--lg .tec--btn::attr(href)").get()


# Requisito 4
def get_url(selector):
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    return url


def get_title(selector):
    title = selector.css(".tec--article__header__title::text").get()
    return title


def get_timestamp(selector):
    timestamp_selector = ".tec--timestamp__item time::attr(datetime)"
    timestamp = selector.css(timestamp_selector).get()
    return timestamp


def get_summary(selector):
    summary_selector = "div.tec--article__body > p:nth-child(1) *::text"
    summary = selector.css(summary_selector).getall()
    return "".join(summary)


def get_writer(selector):
    selectors = [
        ".tec--timestamp:nth-child(1) a::text",
        ".tec--author__info p:first-child::text",
        ".tec--author__info p:first-child a::text",
    ]
    selected = []
    for curr_selector in selectors:
        selected_writer = selector.css(curr_selector).get()
        if selected_writer is not None:
            selected.append(selected_writer.strip())
        if selected_writer is None:
            selected.append(None)
    writer = [item for item in selected if item]
    if len(writer) == 0:
        return None
    return writer[0]


def get_shares_count(selector):
    shares = selector.css(".tec--toolbar div:first-child::text").get()
    if shares is None or not ("Compartilharam") in shares:
        return 0
    shares_count = re.findall(r"\s(\d*)\s(...*)", shares)
    return int(shares_count[0][0])


def get_comments_count(selector):
    comments = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments is None:
        return 0
    return int(comments)


def get_sources(selector):
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    return [item.strip() for item in sources]


def get_categories(selector):
    categories = selector.css("#js-categories a::text").getall()
    return [item.strip() for item in categories]


def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    scraped_news = {
        "url": get_url(selector),
        "title": get_title(selector),
        "timestamp": get_timestamp(selector),
        "writer": get_writer(selector),
        "shares_count": get_shares_count(selector),
        "comments_count": get_comments_count(selector),
        "summary": get_summary(selector),
        "sources": get_sources(selector),
        "categories": get_categories(selector),
    }

    return scraped_news


# Requisito 5
def get_tech_news(amount):
    news = []
    html = fetch("https://www.tecmundo.com.br/novidades")

    news.extend(scrape_novidades(html))

    while len(news) <= amount:
        next_page_link = scrape_next_page_link(html)
        next_page = fetch(next_page_link)
        news.extend(scrape_novidades(next_page))

    result = []

    for item in news[:amount]:
        page = fetch(item)
        result.append(scrape_noticia(page))

    create_news(result)
    return result
