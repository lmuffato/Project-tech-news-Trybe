from parsel import Selector
import requests
import time
from .database import create_news


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
    return selector.css(
        'h3.tec--card__title a.tec--card__title__link::attr(href)'
    ).getall()
    """ links_list = []
    for link in selector.css("h3.tec--card__title"):
        links = link.css("a.tec--card_title_link::attr(href)").get()
        links_list.append(links)
    return links_list """


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css("a.tec--btn::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    # source: https://github.com/tryber/sd-010-a-tech-news/pull/33/files
    # *::text usar no seletor qndo houver tag ancestral
    selector = Selector(html_content)

    url = selector.css('head link[rel=canonical]::attr(href)').get()

    title = selector.css('.tec--article__header__title::text').get()

    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()

    writer = selector.css(".z--font-bold *::text").get()
    if writer:
        writer = writer.strip()

    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count:
        shares_count = int(shares_count.strip()[0])
    else:
        shares_count = 0

    comments_count = selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get()

    summary = ''.join(
        selector.css(
            ".tec--article__body > p:nth-child(1) *::text"
        ).getall()
    )

    sources = [
        source.strip()
        for source in selector.css(
            ".z--mb-16 .tec--badge::text"
        ).getall()
    ]

    categories = [
        category.strip()
        for category in selector.css(
            "#js-categories a::text"
        ).getall()
    ]

    return {
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


# Requisito 5
def get_tech_news(amount):
    new_list = []
    html = fetch("https://www.tecmundo.com.br/novidades")

    new_list.extend(scrape_novidades(html))

    while len(new_list) <= amount:
        next_page_link = scrape_next_page_link(html)
        next_page = fetch(next_page_link)
        new_list.extend(scrape_novidades(next_page))

    result = []

    for item in new_list[:amount]:
        page = fetch(item)
        result.append(scrape_noticia(page))

    create_news(result)
    return result
