from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if (response.status_code == 200):
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    try:
        selector = Selector(html_content)
        return selector.css("h3.tec--card__title a::attr(href)").getall()
    except requests.ReadTimeout:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    selector.css("h3.tec--card__title a::attr(href)").getall()
    show_more_news = selector.css(".tec--list a.tec--btn::attr(href)").get()
    if (show_more_news):
        return show_more_news
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css(
        "div.tec--timestamp__item time::attr(datetime)").get()
    writer = selector.css(
        ".tec--author__info__link::text").get() or selector.css(
        "div.tec--timestamp__item a::text").get() or selector.css(
            "div.tec--author__info p.z--font-bold::text").get() or None
    shares_count = selector.css(".tec--toolbar__item::text").get() or 0
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
    """Seu código deve vir aqui"""
