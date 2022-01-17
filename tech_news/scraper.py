import requests
import time
from parsel import Selector
from tech_news.database import create_news
from tech_news.project_util import (
    get_writer,
    get_summary,
    get_categories,
    get_comments_counts,
    get_share_counts,
    get_sources,
    strip_list_intems,
)


# Requisito 1
def fetch(url):
    try:
        res = requests.get(url, timeout=2)
        time.sleep(1)
        if res.status_code == 200:
            return res.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """nota importante, a forma de utilizar o xpath foi retirada
    de https://parsel.readthedocs.io/en/latest/usage.html#using-selectors"""
    urls_arr = []
    selector = Selector(html_content)
    cards = selector.css("div .tec--list__item")
    for card in cards:
        url = card.xpath(".//article/figure/a/@href").get()
        urls_arr.append(url)
    return urls_arr


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    btn_next_page = selector.css(".tec--btn.tec--btn--lg.tec--btn--primary")
    url_next_page = btn_next_page.xpath(".//@href").get()
    return url_next_page


# Requisito 4
def scrape_noticia(html_content):
    """
    as query do css/xpath foram retiradas de
    https://devhints.io/xpath
    https://devhints.io/css
    """
    selector = Selector(html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("body .tec--article__header__title::text").get()
    datetime = selector.css(
        "div .tec--timestamp__item time::attr(datetime)"
    ).get()
    writer = get_writer(selector)
    shares_count = get_share_counts(selector)
    comments_count = get_comments_counts(selector)
    summary = get_summary(selector)
    categories = get_categories(selector)
    sources = get_sources(selector, categories)

    data = {
        "url": url,
        "title": title,
        "timestamp": datetime,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": strip_list_intems(sources),
        "categories": strip_list_intems(categories),
    }
    return data


# Requisito 5
def get_first_n_urls(amount):
    URL = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(URL)
    url_arr = [*scrape_novidades(html_content)]

    while len(url_arr) < amount:
        next_page_link = scrape_next_page_link(html_content)
        next_page = fetch(next_page_link)
        url_arr = [*url_arr, *scrape_novidades(next_page)]
        html_content = next_page

    return url_arr[:amount]


def get_news_info_by_batch(url_list):
    news_list = []
    for url in url_list:
        content = fetch(url)
        news_info = scrape_noticia(content)
        news_list.append(news_info)
    return news_list


def get_tech_news(amount):
    news_url = get_first_n_urls(amount)
    to_return = get_news_info_by_batch(news_url)
    create_news(to_return)
    print(to_return)
    return to_return


print(scrape_noticia(fetch("https://www.tecmundo.com.br/dispositivos-moveis/215245-remover-conta-mi-cloud-dispositivo-xiaomi.htm")))
