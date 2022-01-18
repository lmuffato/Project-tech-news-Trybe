from parsel import Selector
import requests
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, verify=False, timeout=3)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.exceptions.ReadTimeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    return selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    link = selector.css("div.tec--list a.tec--btn::attr(href)").get()

    if link:
        return link
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    newurl = selector.css("meta[property='og:url']::attr(content)").get()
    newtitle = selector.css(".tec--article__header__title::text").get()
    newtimestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    newwriter1 = selector.css(".tec--author__info__link::text").get()
    newwriter2 = selector.css("div.tec--timestamp__item a::text").get()
    newwriter3 = selector.css(
        "div.tec--author__info p.z--font-bold::text"
    ).get()
    new_shares_count = selector.css(".tec--toolbar__item::text").get()
    new_comments_count = selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get()
    newsummary = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    newsources = [
        item.strip()
        for item in selector.css("div.z--mb-16 div a::text").getall()
    ]
    newcategories = [
        item.strip()
        for item in selector.css("#js-categories a::text").getall()
    ]

    if newwriter1:
        writer = newwriter1
    elif newwriter2:
        writer = newwriter2
    else:
        writer = newwriter3

    return {
        "url": newurl,
        "title": newtitle,
        "timestamp": newtimestamp,
        "writer": writer.strip() if writer else None,
        "shares_count": int(new_shares_count.split()[0])
        if new_shares_count
        else 0,
        "comments_count": int(new_comments_count) if new_comments_count else 0,
        "summary": newsummary,
        "sources": newsources,
        "categories": newcategories,
    }


# Requisito 5
def get_tech_news(amount):
    aux = 0
    URL = "https://www.tecmundo.com.br/novidades"
    info_db = []

    while aux < amount:
        content = fetch(URL)
        news = scrape_novidades(content)
        for new in news:
            info_db.append(scrape_noticia(fetch(new)))
            aux += 1
            if aux % 10 == 0:
                URL = scrape_next_page_link(content)
            if aux == amount:
                break

    create_news(info_db)
    return info_db
