import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    link_selector = ".tec--list__item .tec--card__title__link::attr(href)"
    list = selector.css(link_selector).getall()
    if not list:
        return []
    else:
        return list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link_selector = ".tec--list .tec--btn.tec--btn--primary::attr(href)"
    next_page_link = selector.css(link_selector).get()
    if not next_page_link:
        return None
    else:
        return next_page_link


def unique_css_selector(selector, css_selector):
    return selector.css(css_selector).get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    s = selector

    url = unique_css_selector(s, "meta[property='og:url']::attr(content)")
    title = unique_css_selector(s, "h1.tec--article__header__title::text")
    timestamp = unique_css_selector(s, "time#js-article-date::attr(datetime)")
    writer = unique_css_selector(s, ".z--font-bold *::text")

    if writer:
        writer = writer.strip()

    shares_count_selector = ".tec--toolbar__item:first-child::text"
    shares_count_selected = unique_css_selector(s, shares_count_selector)
    shares_count = 0

    if shares_count_selected:
        shares_count_selected = shares_count_selected.strip()
        shares_count = int(shares_count_selected.split(' ')[0])

    c_c_selected = unique_css_selector(s, "#js-comments-btn::attr(data-count)")
    comments_count = int(c_c_selected)
    summary_selector = ".tec--article__body p:first-child *::text"
    summary_list = selector.css(summary_selector).getall()
    summary = "".join(summary_list)
    sources_list = selector.css(".z--mb-16 .tec--badge::text").getall()
    sources = []

    for source in sources_list:
        sources.append(source.strip())

    categories_list = selector.css("#js-categories .tec--badge::text").getall()
    categories = []

    for category in categories_list:
        categories.append(category.strip())

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
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
