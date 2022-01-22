import requests
import time
from parsel import Selector


# Requisito 1
limit_time = 3
status_ok = 200
time_sleep_function = 1


def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(time_sleep_function)
    try:
        res = requests.get(url, timeout=limit_time)
        if (res.status_code == status_ok):
            return res.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url_list = selector.css('h3.tec--card__title a::attr(href)').getall()
    if (url_list):
        return url_list
    return []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css('div.tec--list a.tec--btn::attr(href)').get()
    if (not next_page):
        return None
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css('head link[rel=canonical]::attr(href)').get()
    title = selector.css('h1.tec--article__header__title::text').get()
    timestamp = selector.css(
        'div.tec--timestamp__item time::attr(datetime)'
        ).get()
    writer = selector.css('.z--font-bold *::text').get()
    author = writer.strip() if writer else None
    shares_count = selector.css('div.tec--toolbar__item::text').get()
    comments_count = selector.css('#js-comments-btn::attr(data-count)').get()
    summary = ''.join(
        selector.css('.tec--article__body > p:first-child *::text'
                     ).getall())
    sources = []
    for source in selector.css('div.z--mb-16 a.tec--badge::text').getall():
        sources.append(source.strip())
    categories = []
    for category in selector.css('#js-categories a::text').getall():
        categories.append(category.strip())
    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': author,
        'shares_count': int(shares_count.strip()[0]) if shares_count else 0,
        'comments_count': int(comments_count) if comments_count else 0,
        'summary': summary,
        'sources': sources,
        'categories': categories,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
