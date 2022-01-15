import time
import requests
from parsel import Selector
from tech_news.database import create_news


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


# Requisito 2 src: https://parsel.readthedocs.io/en/latest/usage.html
def scrape_novidades(html_content):
    data = Selector(html_content)
    return data.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css("div.tec--list a.tec--btn::attr(href)").get()

    if next_page_link:
        return next_page_link
    else:
        return None


# Requisito 4

def scrape_noticia(html_content):
    selector = Selector(html_content)

    site_url = selector.css("meta[property='og:url']::attr(content)").get()
    site_title = selector.css(".tec--article__header__title::text").get()
    get_timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
        ).get()
    writer_1 = selector.css(".tec--author__info__link::text").get()
    writer_2 = selector.css("div.tec--timestamp__item a::text").get()
    writer_3 = selector.css("div.tec--author__info p.z--font-bold::text").get()
    if writer_1:
        writer = writer_1
    elif writer_2:
        writer = writer_2
    else:
        writer = writer_3
    shares_count = selector.css(".tec--toolbar__item::text").get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary = "".join(selector.css(
        ".tec--article__body > p:first-child *::text"
        ).getall())
    # src: https://www.tutorialspoint.com/python3/string_strip.htm
    sources = [item.strip() for item in selector.css(
        "div.z--mb-16 div a::text"
        ).getall()]
    categories = [item.strip() for item in selector.css(
        "#js-categories a::text"
        ).getall()]

    return {
       "url": site_url,
       "title": site_title,
       "timestamp": get_timestamp,
       "writer": writer.strip() if writer else None,
       "shares_count": int(shares_count.split()[0]) if shares_count else 0,
       "comments_count": int(comments_count) if comments_count else 0,
       "summary": summary,
       "sources": sources,
       "categories": categories,
    }


# Requisito 5
def get_tech_news(amount):
    URL = "https://www.tecmundo.com.br/novidades"
    count = 0
    data_arr = []

    while count < amount:
        content = fetch(URL)
        news = scrape_novidades(content)
        for new in news:
            data_arr.append(scrape_noticia(fetch(new)))
            count += 1
            if count % 10 == 0:
                URL = scrape_next_page_link(content)
            if count == amount:
                break

    create_news(data_arr)
    return data_arr
