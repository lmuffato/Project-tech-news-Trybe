import requests
from tech_news.database import create_news
from parsel import Selector
import time

BASE_URL = "https://www.tecmundo.com.br/novidades"


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        response = None
    finally:
        if response is not None and response.status_code == 200:
            return response.text
        else:
            response = None
            return response


# Requisito 2
def scrape_novidades(html_content):
    list_url = []
    if html_content is not None or html_content != '':
        selector = Selector(text=html_content)
        links = selector.css("div.tec--card__info h3 a::attr(href)").getall()
        for link in links:
            list_url.append(link)

    return list_url


# Requisito 3
def scrape_next_page_link(html_content):
    link = None
    if html_content is not None or html_content != '':
        selector = Selector(text=html_content)
        next_page = selector.css("div.tec--list a.tec--btn::attr(href)").get()
        if next_page != '':
            link = next_page

    return link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    writer1 = selector.css(".tec--author__info__link::text").get()
    writer2 = selector.css("div.tec--timestamp__item a::text").get()
    writer3 = selector.css("div.tec--author__info p.z--font-bold::text").get()
    shares_count = selector.css("div.tec--toolbar__item::text").get()
    comments_count = selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get()
    summary = "".join(selector.css(
        "div.tec--article__body > p:first-child *::text"
    ).getall())
    sources = [item.strip() for item in selector.css(
        "div.z--mb-16 div a::text"
    ).getall()]
    categories = [item.strip() for item in selector.css(
        "div#js-categories a::text"
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
    news_db = []
    aux = 0
    URL = BASE_URL

    while aux < amount:
        response = fetch(URL)
        news = scrape_novidades(response)
        for new in news:
            news_db.append(scrape_noticia(fetch(new)))
            aux += 1
            if aux % 10 == 0:
                URL = scrape_next_page_link(response)
            if aux == amount:
                break

    create_news(news_db)
    return news_db
