import requests
import time
from parsel import Selector
from .database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if (response.status_code == 200):
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    content = Selector(html_content)
    return content.css("h3.tec--card__title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    content = Selector(html_content)
    next_page = content.css(".tec--list a.tec--btn::attr(href)").get()

    if (next_page):
        return next_page
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    content = Selector(html_content)

    url = content.css("meta[property='og:url']::attr(content)").get()
    # Ref https://github.com/tryber/sd-010-a-tech-news/pull/65/files

    title = content.css("#js-article-title::text").get()
    timestamp = content.css("#js-article-date::attr(datetime)").get()
    writer = content.css(".z--font-bold *::text").get()
    shares_count = content.css(".tec--toolbar__item::text").get()
    comments_count = content.css("#js-comments-btn::attr(data-count)").get()

    summary = "".join(
        content.css(".tec--article__body > p:first-child *::text")
        .getall()).strip()
    # Ref https://github.com/tryber/sd-010-a-tech-news/pull/65/files

    sources_list = content.css(".z--mb-16 a.tec--badge::text").getall()
    sources = [source.strip() for source in sources_list]
    categories_list = content.css("#js-categories a::text").getall()
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
    news = []
    URL = 'https://www.tecmundo.com.br/novidades'
    content = fetch(URL)
    news_links = scrape_novidades(content)

    while len(news_links) < amount:
        next_page_link = scrape_next_page_link(content)
        next_page_content = fetch(next_page_link)
        news_links.extend(scrape_novidades(next_page_content))

    for link in news_links[:amount]:
        new_page = fetch(link)
        notice_doc = scrape_noticia(new_page)
        news.append(notice_doc)

    create_news(news)
    return news
