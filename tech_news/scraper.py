import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css('#js-article-date::attr(datetime)').get()

    writer = selector.css('.z--font-bold *::text').get()
    if writer:
        writer = writer.strip()
    else:
        writer = None

    shares = selector.css('.tec--toolbar__item::text').get()
    if shares:
        shares_count = shares.split()[0]
    else:
        shares_count = 0

    comments_count = selector.css('#js-comments-btn::attr(data-count)').get()
    summary = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
        ).strip()
    getSources = selector.css(".z--mb-16 .tec--badge::text").getall()
    sources = map(str.strip, getSources)
    getCategories = selector.css("#js-categories a::text").getall()
    categories = map(str.strip, getCategories)

    scraped_news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": list(sources),
        "categories": list(categories),
    }
    return scraped_news


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--list article h3 a::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--list > a::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    news_list = []
    url = "https://www.tecmundo.com.br/novidades"
    while len(news_list) < amount:
        content = fetch(url)
        news_links = scrape_novidades(content)
        for link in news_links:
            link_content = fetch(link)
            scraped_news = scrape_noticia(link_content)
            if len(news_list) < amount:
                news_list.append(scraped_news)
        url = scrape_next_page_link(content)
    create_news(news_list)
    return news_list
