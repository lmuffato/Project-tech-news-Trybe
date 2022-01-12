import requests
import time
from parsel import Selector
from .database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    else:
        if response.status_code == 200:
            return response.text
        else:
            return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    news_item = selector.css('.tec--list__item')
    news_url = []
    for item in news_item:
        url = item.css('article figure a::attr(href)').get()
        news_url.append(url)
    return news_url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link_css_selector = '.tec--list.tec--list--lg > a::attr(href)'
    next_page_link = selector.css(next_page_link_css_selector).get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    title = selector.css('h1.tec--article__header__title::text').get()
    comments_count = selector.css('#js-comments-btn::text').re_first(r"\d+")
    shares_count = selector.css('.tec--toolbar__item::text').re_first(r"\d+")
    if not shares_count:
        shares_count = 0
    raw_content_writer = selector.css('.z--font-bold ::text').get()
    if not raw_content_writer:
        writer = None
    else:
        writer = raw_content_writer.strip()
    timestamp = selector.css('time#js-article-date::attr(datetime)').get()
    css_selector = '.tec--article__body > p:first_child *::text'
    raw_content_summary = selector.css(css_selector).getall()
    summary = "".join(raw_content_summary).strip()
    raw_content_sources = selector.css('.z--mb-16 a.tec--badge::text').getall()
    sources = [src.strip() for src in raw_content_sources]
    raw_content_categories = selector.css('div#js-categories a::text').getall()
    categories = [cat.strip() for cat in raw_content_categories]
    url = selector.css('head link[rel=canonical]::attr(href)').get()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count) or 0,
        "comments_count": int(comments_count) or 0,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
def get_tech_news(amount):
    recovered_news = []
    next_page_link = 'https://www.tecmundo.com.br/novidades'
    while len(recovered_news) != amount:
        html_content = fetch(next_page_link)
        news_urls = scrape_novidades(html_content)
        for url in news_urls:
            if len(recovered_news) == amount:
                break
            page_content = fetch(url)
            news_data = scrape_noticia(page_content)
            recovered_news.append(news_data)
        next_page_link = scrape_next_page_link(html_content)
    create_news(recovered_news)
    return recovered_news
