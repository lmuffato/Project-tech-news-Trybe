import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        request = requests.get(url, timeout=3)
        time.sleep(1)
        if request.status_code == 200:
            return request.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    if selector:
        return selector.css(
                "h3.tec--card__title a.tec--card__title__link::attr(href)"
                ).getall()
    else:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    more = selector.css("div.tec--list a.tec--btn::attr(href)").get()
    if more:
        return more
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".z--font-bold ::text").get()
    if writer:
        # https://careerkarma.com/blog/python-string-strip/
        writer = writer.strip()
    else:
        writer = None

    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count:
        shares_count = int((shares_count.strip()).split(" ")[0])
    else:
        shares_count = 0

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments_count:
        comments_count = int(comments_count)
    else:
        comments_count = 0

    summary = "".join(selector.css(
        ".tec--article__body > p:first-child *::text").getall())

    sources = [src.strip() for src in selector.css(
        ".z--mb-16 div a.tec--badge::text").getall()]

    categories = [category.strip() for category in selector.css(
        "#js-categories .tec--badge::text").getall()]

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
