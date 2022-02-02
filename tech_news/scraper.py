import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    list_news = selector.css(
        'h3.tec--card__title a.tec--card__title__link::attr(href)'
    ).getall()
    if len(list_news) == 0:
        return []
    return list_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_pag_url = selector.css('a.tec--btn::attr(href)').get()
    if next_pag_url == "":
        return None
    return next_pag_url


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    link = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".z--font-bold *::text").get()
    shares_count = selector.css(".tec--toolbar__item::text").get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary = ''.join(
        selector.css(".tec--article__body > p:first-child *::text")
        .getall()).strip()
    sources_list = selector.css(".z--mb-16 a.tec--badge::text").getall()
    sources = [source.strip() for source in sources_list]
    categories_list = selector.css("#js-categories a::text").getall()
    categories = [category.strip() for category in categories_list]

    return {
        "url": link,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip() if writer else None,
        "shares_count": int(shares_count.split()[0]) if shares_count else 0,
        "comments_count": int(comments_count) if comments_count else 0,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }

    # Ref https://github.com/tryber/sd-010-a-tech-news/pull/115/files


# Requisito 5
def get_tech_news(amount):
    URL = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(URL)
    news_dict = []

    last_news_url = scrape_novidades(html_content)

    while len(last_news_url) < amount:
        next_page_link = scrape_next_page_link(html_content)
        next_page = fetch(next_page_link)
        news_links = scrape_novidades(next_page)

        for news in news_links:
            last_news_url.append(news)

    for url_news in last_news_url[:amount]:
        page = fetch(url_news)
        news_dict.append(scrape_noticia(page))

    create_news(news_dict)
    
    return news_dict

    # Ref https://github.com/tryber/sd-010-a-tech-news/pull/111/files
