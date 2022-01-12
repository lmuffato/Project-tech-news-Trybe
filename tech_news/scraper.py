from parsel import Selector
import requests
import time
import re


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if (response.status_code == 200):
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls = []
    for item in selector.css(".tec--list__item"):
        url = item.css(".tec--card__info h3 a::attr(href)").get()
        urls.append(url)
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--btn::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.xpath('//link[contains(@rel, "canonical")]/@href').get()
    writer = selector.css(".z--font-bold ::text").get()
    if writer:
        writer = writer.strip()
    else:
        writer = None

    shares_str = selector.css("#js-author-bar nav div::text").get()
    if shares_str:
        shares_num = int(re.findall(r"\d+", shares_str)[0])
    else:
        shares_num = 0

    comments = selector.css("#js-comments-btn::attr(data-count)").get()

    sources = []
    for item in selector.css(".z--mb-16 .tec--badge::text").getall():
        sources.append(item.strip())

    categories = []
    for i in selector.css("#js-categories a::text").getall():
        categories.append(i.strip())

    s = selector.css(".tec--article__body p:first-child *::text").getall()
    response = {
        "url": url,
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("time::attr(datetime)").get(),
        "writer": writer,
        "shares_count": shares_num,
        "comments_count": int(comments),
        "summary": "".join(s),
        "sources": sources,
        "categories": categories
    }
    return response


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
