import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    if html_content == "":
        return []
    selector = Selector(text=html_content)
    list = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 > div.tec--list"
        ".tec--list--lg article > div > h3 > a ::attr(href)"
    ).getall()
    return list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 > "
        "div.tec--list.tec--list--lg > a ::attr(href)"
    ).get()
    return link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("head > link[rel=canonical] ::attr(href)").get()
    title = selector.css("#js-article-title ::text").get()
    timestamp = selector.css("#js-article-date ::attr(datetime)").get()
    author = selector.css(".tec--author__info__link ::text").get()
    shares = selector.css(".tec--toolbar__item ::text").get()
    comments = selector.css("#js-comments-btn ::attr(data-count)").get()
    summary = selector.css(
        ".tec--article__body > p:first_child *::text"
    ).getall()
    sources = selector.css(".tec--badge ::text").getall()
    categories = selector.css("#js-categories ::text").getall()
    print(categories)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
