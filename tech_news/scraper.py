import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)

        if (response.status_code != 200):
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    links = selector.css(
        'h3.tec--card__title a.tec--card__title__link::attr(href)').getall()
    if(len(links) == 0):
        return []
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page = selector.css('a.tec--btn::attr(href)').get()
    if(next_page):
        return next_page
    return None


def writerLogic(selector):
    if selector.css(".tec--author__info__link ::text").get():
        writer = selector.css(".tec--author__info__link ::text").get()
        return writer
    if selector.css(".tec--timestamp__item a::text").get():
        writer = selector.css(".tec--timestamp__item a::text").get()
        return writer
    if selector.css(".z--m-none ::text").get():
        writer = selector.css(".z--m-none ::text").get()
        return writer


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css("head link[rel=canonical] ::attr(href)").get()
    title = selector.css('h1.tec--article__header__title::text').get()
    data = selector.css('time::attr(datetime)').get()
    shares_count = selector.css(
        'div.tec--toolbar__item::text').re_first(r'\d+')
    comments_count = selector.css('button::attr(data-count)').re_first(r'\d+')
    summary = selector.css(
        'div.tec--article__body> p:first-child *::text').getall()
    sources = selector.css('div.z--mb-16 div > a::text').getall()
    categories = selector.css("a.tec--badge--primary ::text").getall()
    categoriesList = []

    for category in categories:
        categoriesList.append(category.strip())

    sourceList = []

    for source in sources:
        sourceList.append(source.strip())
    writer = writerLogic(selector).strip()

    scrap_dict = {
        "url": url,
        "title": title,
        "timestamp": data,
        "writer": writer
        if writer else None,
        "shares_count": int(shares_count) if shares_count else 0,
        "comments_count": int(comments_count) if comments_count else 0,
        "summary": ''.join(str(item) for item in summary),
        "sources": sourceList,
        "categories": categoriesList
        }
    return scrap_dict


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
