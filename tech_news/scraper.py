import requests
import time
from parsel import Selector


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    links = selector.css(".tec--card__info h3 a::attr(href)").getall()

    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    pagination = selector.css(".tec--list a.tec--btn::attr(href)").get()

    return pagination


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css(".tec--article__header__title::text").get()
    time = selector.css(".tec--timestamp__item time::attr(datetime)").get()

    writer_selector = selector.css(".z--font-bold *::text").get()
    writer = writer_selector.strip() if writer_selector else None

    shares_selector = selector.css(".tec--toolbar__item::text").get()
    shares_count = int(shares_selector.split()[0]) if shares_selector else 0

    comment_selector = selector.css("#js-comments-btn::attr(data-count)").get()
    comments_count = int(comment_selector) if comment_selector else 0

    summary_selector = ".tec--article__body p:first-child *::text"
    summary = "".join(selector.css(summary_selector).getall()).strip()

    sources_selector = ".z--mb-16 a.tec--badge::text"
    sources_list = selector.css(sources_selector).getall()
    sources = [source.strip() for source in sources_list]

    categories_selector = "#js-categories a::text"
    categories_list = selector.css(categories_selector).getall()
    categories = [category.strip() for category in categories_list]

    return {
        "url": url,
        "title": title,
        "timestamp": time,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
