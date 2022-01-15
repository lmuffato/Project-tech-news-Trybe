import requests
import time
from parsel import Selector


# Requisito 1
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
    data = Selector(html_content)
    return data.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
        ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    see_more_news_btn = selector.css(".tec--list a.tec--btn::attr(href)").get()
    if (see_more_news_btn):
        return see_more_news_btn
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".z--font-bold *::text").get()
    shares_count = selector.css(".tec--toolbar__item::text").get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()

    summary_css_selector = ".tec--article__body > p:first-child *::text"
    summary = "".join(selector.css(summary_css_selector).getall()).strip()

    sources_css_selector = ".z--mb-16 a.tec--badge::text"
    sources_list = selector.css(sources_css_selector).getall()
    sources = [source.strip() for source in sources_list]

    categories_css_selector = "#js-categories a::text"
    categories_list = selector.css(categories_css_selector).getall()
    categories = [category.strip() for category in categories_list]

    data = {
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

    return data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
