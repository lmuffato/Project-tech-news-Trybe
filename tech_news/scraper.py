import requests
import time
from parsel import Selector
from .database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
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
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    links = selector.css(".tec--card__info h3 a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    pagination = selector.css(".tec--list a.tec--btn::attr(href)").get()
    return pagination


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    writer = selector.css(".z--font-bold *::text").get().strip()

    shares_count = selector.css(".tec--toolbar__item::text").get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()

    summary_selector = ".tec--article__body > p:first-child *::text"
    summary = "".join(selector.css(summary_selector).getall()).strip()

    sources_selector = ".z--mb-16 a.tec--badge::text"
    sources_list = selector.css(sources_selector).getall()
    sources = [source.strip() for source in sources_list]

    categories_selector = "#js-categories a::text"
    categories_list = selector.css(categories_selector).getall()
    categories = [category.strip() for category in categories_list]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer if writer else None,
        "shares_count": int(shares_count.split()[0]) if shares_count else 0,
        "comments_count": int(comments_count) if comments_count else 0,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    news = []
    URL = "https://www.tecmundo.com.br/novidades"
    content = fetch(URL)
    news_links = scrape_novidades(content)

    while len(news_links) < amount:
        next_page_link = scrape_next_page_link(content)
        next_content = fetch(next_page_link)
        news_links.extend(scrape_novidades(next_content))

    for link in news_links[:amount]:
        new_content = fetch(link)
        data = scrape_noticia(new_content)
        news.append(data)

    create_news(news)
    return news
