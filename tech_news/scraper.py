import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    list_href = selector.css(
        ".tec--list .tec--card .tec--card__info \
            .tec--card__title a[href*=htm]::attr(href)"
    ).getall()
    return list_href


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    list_href = selector.css(".tec--list a[href*=page]::attr(href)").get()
    return list_href


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css("head meta[content*=tecmundo]::attr(content)").get()
    title = selector.css("head meta[property*=title]::attr(content)").get()
    timestamp = selector.css("time::attr(datetime)").get()
    writer = selector.css(".z--font-bold *::text").get()
    if writer is not None:
        writer = writer.strip()
    shares_count = selector.css(
        ".tec--toolbar .tec--toolbar__item::text"
    ).get()
    if shares_count is not None:
        shares_count = int(shares_count.strip()[0])
    else:
        shares_count = 0
    comments_count = selector.css(
        ".tec--toolbar .tec--toolbar__item::text"
    ).get()
    if comments_count is not None:
        comments_count = int(comments_count.strip()[0])
    else:
        comments_count = 0
    summary = selector.css("head meta[name*=description]::attr(content)").get()
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    categories = selector.css(".tec--badge--primary *::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": [source.strip() for source in sources],
        "categories": [cat.strip() for cat in categories],
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
