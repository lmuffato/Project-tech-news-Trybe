import time
import requests
from parsel import Selector
from .database import create_news


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
    selector = Selector(html_content)
    news_item = selector.css('.tec--list__item')
    news_url = []
    for item in news_item:
        url = item.css('article figure a::attr(href)').get()
        news_url.append(url)
    return news_url


# Requisito 3
def scrape_next_page_link(html_content):
    link = None
    if html_content is not None or html_content != '':
        selector = Selector(text=html_content)
        next_page = selector.css("div.tec--list a.tec--btn::attr(href)").get()
        if next_page != '':
            link = next_page
    return link


# Requisito 4
def scrape_noticia(html_content):
    data = Selector(text=html_content)
    news_url = data.css("meta[property='og:url']::attr(content)").get()
    news_title = data.css("h1.tec--article__header__title::text").get()
    news_timestamp = data.css(
        "div.tec--timestamp__item time::attr(datetime)"
    ).get()
    news_writer = (
        data.css(".tec--author__info__link::text").get()
        or data.css("div.tec--timestamp__item a::text").get()
        or data.css("div.tec--author__info p.z--font-bold::text").get()
    )
    news_shares_count = data.css(".tec--toolbar__item::text").get()
    news_comments_count = data.css("#js-comments-btn::attr(data-count)").get()
    news_summary = "".join(
        data.css(".tec--article__body > p:first-child *::text").getall()
    )
    news_sources = [
        item.strip() for item in data.css("div.z--mb-16 div a::text").getall()
    ]
    news_categories = [
        item.strip() for item in data.css("#js-categories a::text").getall()
    ]
    news_data = {
        "url": news_url,
        "title": news_title,
        "timestamp": news_timestamp,
        "writer": news_writer.strip() if news_writer else None,
        "shares_count": int(news_shares_count.split()[0])
        if news_shares_count
        else 0,
        "comments_count": int(news_comments_count)
        if news_comments_count
        else 0,
        "summary": news_summary,
        "sources": news_sources,
        "categories": news_categories,
    }
    return news_data


# Requisito 5
def get_tech_news(amount):
    tecmundo_url = fetch("https://www.tecmundo.com.br/novidades")
    links_notes = scrape_novidades(tecmundo_url)

    while len(links_notes) < amount:
        more_pages = scrape_next_page_link(tecmundo_url)
        next_page_info = fetch(more_pages)
        links_notes.extend(scrape_novidades(next_page_info))

    notes = []
    for element in links_notes[:amount]:
        new_page_code = fetch(element)
        new_note = scrape_noticia(new_page_code)
        notes.append(new_note)
    create_news(notes)
    return notes
