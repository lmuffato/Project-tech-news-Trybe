import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    parsel_selector = Selector(html_content)
    list = []
    for news in parsel_selector.css("div.tec--list__item"):
        element_link = news.css("a.tec--card__title__link::attr(href)").get()
        list.append(element_link)
    return list


# Requisito 3
def scrape_next_page_link(html_content):
    parsel_selector = Selector(html_content)
    next_page_link = parsel_selector.css(
        "a.tec--btn--primary::attr(href)"
    ).get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    parsel_selector = Selector(html_content)
    url = parsel_selector.css("head link[rel=canonical]::attr(href)").get()
    title = parsel_selector.css("#js-article-title::text").get()
    timestamp = parsel_selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()

    writer = parsel_selector.css(".z--font-bold *::text").get()
    if writer:
        writer = writer.strip()

    shares_count = parsel_selector.css(".tec--toolbar__item::text").get()
    if shares_count:
        shares_count = int(shares_count.strip()[0])
    else:
        shares_count = 0

    comments_count = parsel_selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get()

    summary = ''.join(
        parsel_selector.css(
            ".tec--article__body > p:nth-child(1) *::text"
        ).getall()
    )

    sources = [
        source.strip()
        for source in parsel_selector.css(
            ".z--mb-16 .tec--badge::text"
        ).getall()
    ]

    categories = [
        category.strip()
        for category in parsel_selector.css(
            "#js-categories a::text"
        ).getall()
    ]

    scraping_data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories
    }
    return scraping_data


# Requisito 5
def get_tech_news(amount):
    html_content = fetch("https://www.tecmundo.com.br/novidades")
    url = []
    news_links = []
    url.extend(scrape_novidades(html_content))

    while len(url) < amount:
        next_page_link = scrape_next_page_link(html_content)
        next_page = fetch(next_page_link)
        url.extend(scrape_novidades(next_page))

    for i in url[:amount]:
        news = fetch(i)
        news_links.append(scrape_noticia(news))

    create_news(news_links)
    return news_links
