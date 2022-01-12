import requests
from requests.exceptions import Timeout
import time
from parsel import Selector


# Requisito 1
# GO!
def fetch(url):
    try:
        time.sleep(1)
        request = requests.get(url, timeout=3)
        if request.status_code == 200:
            return request.text
        else:
            return None
    except Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    urls = selector.css(
        ".tec--list .tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css(".tec--list a.tec--btn::attr(href)").get()
    if next_page_link:
        return next_page_link
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news_dict = {
        "url": selector.css('meta[property="og:url"]::attr(content)').get(),
        "title": selector.css("h1.tec--article__header__title::text").get(),
        "timestamp": selector.css(
            ".tec--timestamp__item time::attr(datetime)"
        ).get(),
        "writer": selector.css("a.tec--author__info__link::text")
        .get()
        .strip(),
        "shares_count": int(
            selector.css(".tec--toolbar__item::text").get().strip().split()[0]
        ),
        "comments_count": int(
            selector.css(
                ".tec--toolbar__item #js-comments-btn::attr(data-count)"
            ).get()
        ),
        "summary": selector.css(".tec--article__body p *::text").get(),  # ???
        "sources": [
            badge.strip()
            for badge in selector.css(
                '.tec--badge[rel="noopener nofollow"]::text'
            ).getall()
        ],
        "categories": [
            badge.strip()
            for badge in selector.css(
                "#js-categories .tec--badge::text"
            ).getall()
        ],
    }
    return news_dict


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
