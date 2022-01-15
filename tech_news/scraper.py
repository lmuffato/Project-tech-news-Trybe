import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if (response.status_code != 200):
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    page = Selector(html_content)
    css_link_selector = "h3.tec--card__title a::attr(href)"
    return page.css(css_link_selector).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    page = Selector(html_content)
    css_next_page_selector = ".tec--list a.tec--btn::attr(href)"
    next_page_button = page.css(css_next_page_selector).get()

    if (next_page_button):
        return next_page_button
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    page = Selector(html_content)

    url = page.css("meta[property='og:url']::attr(content)").get()
    title = page.css(".tec--article__header__title::text").get()
    timestamp = page.css("#js-article-date::attr(datetime)").get()
    writer = page.css(".z--font-bold *::text").get()
    shares_count = page.css(".tec--toolbar__item::text").get()
    comments_count = page.css("#js-comments-btn::attr(data-count)").get()

    summary_css_selector = ".tec--article__body p:first-child *::text"
    summary = "".join(page.css(summary_css_selector).getall()).strip()

    sources_css_selector = ".z--mb-16 a.tec--badge::text"
    sources_list = page.css(sources_css_selector).getall()
    sources = [source.strip() for source in sources_list]

    categories_css_selector = "#js-categories a::text"
    categories_list = page.css(categories_css_selector).getall()
    categories = [category.strip() for category in categories_list]

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
