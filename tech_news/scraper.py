import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        response.raise_for_status()
    except requests.Timeout:
        return None
    except requests.ConnectionError:
        return None
    except requests.HTTPError:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    list = selector.css(
        ".tec--list__item a.tec--card__title__link::attr(href)"
    ).getall()

    return list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    link = selector.css(
        ".z--row a.z--mx-auto::attr(href)"
    ).get()

    return link


# Requisito 4
def extends_scrape_notia(selector):
    link = selector.css("link[rel*='canonical']::attr(href)").get()

    title = selector.css("#js-article-title::text").get()

    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    writer = (
        selector.css("#js-author-bar .z--font-bold::text").get()
        or selector.css("div#js-author-bar>div>p>a::text").get()
        or selector.css("div.tec--timestamp__item>a::text").get()
    )
    if writer is not None:
        writer = writer.strip()

    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count is None:
        shares_count = 0
    else:
        shares_count = int(shares_count.split(" ")[1])

    comments_count = (
        selector.css(".js-comments-btn::attr(data-count)").get()
        or selector.css("#js-comments-btn::attr(data-count)").get()
    )
    if comments_count is None:
        comments_count = 0
    else:
        comments_count = int(comments_count)
    return {
        "url": link,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
    }


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    css_seletor = "div.tec--article__body-grid>div.tec--article__body"
    summary = (
        selector.css(
            f"{css_seletor}>p:nth-child(1) *::text"
        ).getall()
    )
    summary = "".join(summary)

    sources = selector.css("div.z--mb-16 a.tec--badge::text").getall()
    new_sources = []
    if sources is not None:
        for word in sources:
            new_word = word.split(" ")
            new_word = [word for word in new_word if word != ""]
            new_sources.append(" ".join(new_word))

    categories = selector.css("#js-categories a.tec--badge::text").getall()
    new_categories = []
    if categories is not None:
        for word in categories:
            new_word = word.split(" ")
            new_word = [word for word in new_word if word != ""]
            new_categories.append(" ".join(new_word))

    extend = extends_scrape_notia(selector)

    return {
        "url": extend["url"],
        "title": extend["title"],
        "timestamp": extend["timestamp"],
        "writer": extend["writer"],
        "shares_count": extend["shares_count"],
        "comments_count": extend["comments_count"],
        "summary": summary,
        "sources": new_sources,
        "categories": new_categories,
    }


# Requisito 5
def get_tech_news(amount):
    url_noticias = "https://www.tecmundo.com.br/novidades"
    response = fetch(url_noticias)

    list_noticias = scrape_novidades(response)

    while len(list_noticias) < amount:
        url_nex_page = scrape_next_page_link(response)
        html_nex_page = fetch(url_nex_page)
        new_list = scrape_novidades(html_nex_page)
        list_noticias.extend(new_list)

    noticias = []

    for link in list_noticias:
        html_noticia = fetch(link)
        noticia = scrape_noticia(html_noticia)
        noticias.append(noticia)
        if len(noticias) == amount:
            create_news(noticias)
            break

    return noticias
