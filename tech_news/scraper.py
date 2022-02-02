import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        else:
            return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    # seletor css do tecmundo: h3.tec--card__title  a.tec--card__title__link
    news_links = selector.css(
        'h3.tec--card__title a.tec--card__title__link::attr(href)'
        ).getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    # seletor css do tecmundo:
    # tec--btn tec--btn--lg tec--btn--primary z--mx-auto z--mt-48
    next_link = selector.css('a.tec--btn--lg::attr(href)').get()
    return next_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = selector.css('head link[rel=canonical]::attr(href)').get()
    title = selector.css('h1.tec--article__header__title::text').get()
    timestamp = selector.css(
        'div.tec--timestamp__item time::attr(datetime)'
        ).get()
    writer = selector.css('.z--font-bold *::text').get()

    if writer:
        writer = writer.strip()

    shares_count = selector.css('svg.feather::text').get()
    if shares_count is None:
        shares_count = int(0)
    else:
        shares_count = int(shares_count)
    comments_count = selector.css(
        '#js-comments-btn::attr(data-count)'
        ).get()
    if comments_count is None:
        comments_count = int(0)
    else:
        comments_count = int(comments_count)
    # Summary consultado em outros códigos
    summary = ''.join(
        selector.css('.tec--article__body > p:first-child *::text').getall()
    )
    sources = selector.css('div.z--mb-16 a::text').getall()
    sources = [source.strip() for source in sources]
    categories = selector.css(
        '#js-categories a.tec--badge *::text'
        ).getall()
    categories = [category.strip() for category in categories]
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
        }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
