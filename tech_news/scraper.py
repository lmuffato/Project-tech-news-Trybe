from time import sleep

import requests
from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    "Seu código deve vir aqui"
    sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.exceptions.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    site_content = Selector(html_content)
    links_news = []
    for link in site_content.css("h3.tec--card__title"):
        new_link = link.css("a.tec--card__title__link::attr(href)").get()
        links_news.append(new_link)
    return links_news


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(".tec--list > a::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    result = dict()
    result["url"] = selector.css("link[rel=canonical]::attr(href)").get()
    result["title"] = selector.css(".tec--article__header__title::text").get()
    result["timestamp"] = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    writer = selector.css(".z--font-bold *::text").get().strip()
    result["writer"] = writer
    share_counts = selector.css(".tec--toolbar__item::text").get()
    result["shares_count"] = (
        int(share_counts.strip().split()[0]) if share_counts else 0
    )
    result["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )
    result["summary"] = "".join(
        selector.css(".tec--article__body > p:nth-child(1) ::text").getall()
    )
    result["sources"] = [
        source.strip()
        for source in selector.css(".z--mb-16 div .tec--badge::text").getall()
    ]
    result["categories"] = [
        category.strip()
        for category in selector.css(
            "#js-categories .tec--badge::text"
        ).getall()
    ]
    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    link = fetch("https://www.tecmundo.com.br/novidades")
    result = list()

    while len(result) < amount:
        for url in scrape_novidades(link):
            if len(result) < amount:
                news = fetch(url)
                result.append(scrape_noticia(news))

        if len(result) < amount:
            next_page = scrape_next_page_link(link)
            link = fetch(next_page)

    create_news(result)
    return result
