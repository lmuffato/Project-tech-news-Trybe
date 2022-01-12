import requests
import time
from parsel import Selector
from tech_news.database import create_news

URL_BASE = "https://www.tecmundo.com.br/novidades"


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        else:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
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

    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
        ).get()
    writer1 = selector.css(".tec--author__info__link::text").get()
    writer2 = selector.css("div.tec--timestamp__item a::text").get()
    writer3 = selector.css("div.tec--author__info p.z--font-bold::text").get()
    shares_count = selector.css(".tec--toolbar__item::text").get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary = "".join(selector.css(
        ".tec--article__body > p:first-child *::text"
        ).getall())
    sources = [item.strip() for item in selector.css(
        "div.z--mb-16 div a::text"
        ).getall()]
    categories = [item.strip() for item in selector.css(
        "#js-categories a::text"
        ).getall()]

    if writer1:
        writer = writer1
    elif writer2:
        writer = writer2
    else:
        writer = writer3

    return {
       "url": url,
       "title": title,
       "timestamp": timestamp,
       "writer": writer.strip() if writer else None,
       "shares_count": int(shares_count.split()[0]) if shares_count else 0,
       "comments_count": int(comments_count) if comments_count else 0,
       "summary": summary,
       "sources": sources,
       "categories": categories,
    }


# Requisito 5
def get_tech_news(amount):
    aux = 0
    URL = URL_BASE
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


x = get_tech_news(19)
print(x)
