import time

import requests

from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text

        return None

    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    link = "h3.tec--card__title a::attr(href)"
    data = selector.css(link).getall()

    return data


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    link = "a.tec--btn ::attr(href)"
    data = selector.css(link).get()

    return data


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    return {
        "url": selector.css("meta[property='og:url']::attr(content)").get(),
        "title": selector.css("h1.tec--article__header__title::text").get(),
        "timestamp": selector.css(
          "div.tec--timestamp__item time::attr(datetime)"
          ).get(),
        "writer": (selector.css(
          ".tec--author__info__link::text"
          ).get() or selector.css(
          "div.tec--timestamp__item a::text"
          ).get() or selector.css(
            "div.tec--author__info p.z--font-bold::text"
            ).get() or None).strip() if (selector.css(
              ".tec--author__info__link::text").get() or selector.css(
                "div.tec--timestamp__item a::text").get() or selector.css(
                  "div.tec--author__info p.z--font-bold::text"
                ).get() or None) else None,
        "shares_count": int((selector.css(
          ".tec--toolbar__item::text"
          ).get() or 0).split()[0]) if (selector.css(
            ".tec--toolbar__item::text"
            ).get() or 0) else 0,
        "comments_count": int(selector.css(
          "#js-comments-btn::attr(data-count)"
          ).get()) if selector.css(
            "#js-comments-btn::attr(data-count)").get() else 0,
        "summary": ("".join(selector.css(
          ".tec--article__body > p:first-child *::text"
          ).getall())),
        "sources": [item.strip() for item in selector.css(
          "div.z--mb-16 div a::text"
          ).getall()],
        "categories": [item.strip() for item in selector.css(
          "#js-categories a::text"
          ).getall()],
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    news = []
    list = []

    while len(list) < amount:
        content = fetch(url)
        list.extend(scrape_novidades(content))
        url = scrape_next_page_link(content)

    for link in list:
        content = fetch(link)
        news.append(scrape_noticia(content))

    create_news(news)

    return news
