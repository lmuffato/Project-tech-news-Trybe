import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link = selector.css("a.tec--btn::attr(href)").getall()

    return link[0] if link else None


# Requisito 4
def scrape_noticia(html_content):
    noticia = {}
    selector = Selector(text=html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    noticia["url"] = url
    title = selector.css("h1.tec--article__header__title::text").get()
    noticia["title"] = title
    timestamp = selector.css("time::attr(datetime)").get()
    noticia["timestamp"] = timestamp
    writer = selector.css(".z--font-bold *::text").get()
    noticia["writer"] = writer.strip() if writer else None
    shares_count = selector.css("div.tec--toolbar__item::text").re_first(
        r"\d+"
    )
    noticia["shares_count"] = int(shares_count) if shares_count else 0
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    noticia["comments_count"] = int(comments_count)
    summary = "".join(
        selector.css("div.tec--article__body p:first-child *::text").getall()
    )
    noticia["summary"] = summary
    sources = selector.css("div.z--mb-16 a::text").getall()
    sources = [s.strip() for s in sources]
    noticia["sources"] = sources
    categories = selector.css("div#js-categories a.tec--badge::text").getall()
    categories = [c.strip() for c in categories]
    noticia["categories"] = categories
    return noticia


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
