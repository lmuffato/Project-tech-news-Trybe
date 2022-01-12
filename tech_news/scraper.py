import requests
import time
from parsel import Selector
from tech_news.database import create_news


# https://developer.mozilla.org/pt-BR/docs/Web/CSS/CSS_Selectors
# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None

    if (response.status_code != 200):
        return None

    return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    links_news = selector.css(
        "main .tec--card__title__link::attr(href)"
    ).getall()
    return links_news


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page_link = selector.css(
        ".tec--list.tec--list--lg > a::attr(href)"
    ).get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = (
        selector.css(".tec--author__info__link::text").get()
        or selector.css(".tec--timestamp__item.z--font-bold a::text").get()
        or selector.css(".z--m-none.z--truncate.z--font-bold::text").get()
    )
    # https://www.w3schools.com/python/ref_string_strip.asp
    config_writer = writer.strip() if writer else None
    # print(config_writer)
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    shares_count = int(shares_count) if shares_count else 0
    # print(shares_count)
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d+")
    comments_count = int(comments_count) if comments_count else 0
    # print(comments_count)
    summary = selector.css(
        ".tec--article__body > p:first-of-type *::text"
    ).getall()
    summary = "".join(summary).strip()
    # print(summary)
    sources = selector.css(".z--mb-16 div a::text").getall()
    sources = [source.strip() for source in sources]
    # print(sources)
    categories = selector.css("#js-categories a::text").getall()
    categories = [category.strip() for category in categories]
    # print(categories)

    data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": config_writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }
    # print(data)
    return data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    page = "https://www.tecmundo.com.br/novidades"
    tech_news = []
    while amount > len(tech_news):
        fetch_tech_news = fetch(page)
        pages = scrape_novidades(fetch_tech_news)
        # print(pages)
        for link in pages:
            fetch_link = fetch(link)
            scrape = scrape_noticia(fetch_link)
            # print(scrape)
            tech_news.append(scrape)
            if len(tech_news) == amount:
                break

            page = scrape_next_page_link(fetch_tech_news)
    create_news(tech_news)
    # print(tech_news)
    return tech_news
