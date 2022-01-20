from parsel import Selector
import requests
import time

from .database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None

    except requests.ReadTimeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls = selector.css(
        ".tec--list__item .tec--card__thumb__link::attr(href)"
    ).getall()
    if not urls:
        return []
    else:
        return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    selected_class = ".tec--list .tec--btn::attr(href)"
    next_page_link = selector.css(selected_class).get()
    if not next_page_link:
        return None
    else:
        return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    def scrape_strip(list_item):
        new_list = []
        for item in list_item:
            new_item = item.strip()
            new_list.append(new_item)

        return new_list

    def scrape_join(list_item):
        new_list = "".join(list_item)
        return new_list

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1::text").get()
    writer = selector.css(".z--font-bold ::text").get()
    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    categories = selector.css(".tec--badge--primary ::text").getall()
    comments = selector.css("#js-comments-btn::attr(data-count)").get()
    shares_count = selector.css(".tec--toolbar__item::text").get()
    timestamp = selector.css("time::attr(datetime)").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip() if writer else None,
        "comments_count": int(comments) if comments else 0,
        "shares_count": int(shares_count.split()[0]) if shares_count else 0,
        "summary": scrape_join(summary),
        "sources": scrape_strip(sources),
        "categories": scrape_strip(categories),
    }


# Requisito 5
def get_tech_news(amount):
    urls_base = "https://www.tecmundo.com.br/novidades"

    def fetch_for_page(url):
        response_fetch = fetch(url)
        # link_next_page = scrape_next_page_link(response_fetch)
        return response_fetch

    def quant_noticias(urls_noticias, next_url):
        if len(urls_noticias) < amount:
            more_pages = fetch_for_page(next_url)
            more_link = scrape_novidades(more_pages)
            next_url = scrape_next_page_link(more_pages)
            urls_noticias.extend(more_link)
            quant_noticias(urls_noticias, next_url)

    response_fetch = fetch_for_page(urls_base)
    urls_noticias = scrape_novidades(response_fetch)
    next_url = scrape_next_page_link(response_fetch)
    quant_noticias(urls_noticias, next_url)

    list_noticias = []

    for index in range(amount):
        url = urls_noticias[index]
        noticia = fetch(url)
        resumo = scrape_noticia(noticia)
        list_noticias.append(resumo)

    create_news(list_noticias)
    return list_noticias


data = get_tech_news(20)
print(f" quant {len(data)}")
