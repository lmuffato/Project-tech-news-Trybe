import requests
import time
from parsel import Selector
from .database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if (response.status_code != 200):
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    data = Selector(html_content)
    return data.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css("div.tec--list a.tec--btn::attr(href)").get()
    if next_page_link:
        return next_page_link
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

    summary_selector = ".tec--article__body > p:first-child *::text"
    summary = "".join(page.css(summary_selector).getall()).strip()

    sources_selector = ".z--mb-16 a.tec--badge::text"
    sources_list = page.css(sources_selector).getall()
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
    news = []
    page_content = fetch('https://www.tecmundo.com.br/novidades')
    news_links = scrape_novidades(page_content)

    while len(news_links) < amount:
        next_page_link = scrape_next_page_link(page_content)
        next_page_content = fetch(next_page_link)
        news_links.extend(scrape_novidades(next_page_content))

    for link in news_links[:amount]:
        new_page_content = fetch(link)
        new_data = scrape_noticia(new_page_content)
        news.append(new_data)

    create_news(news)
    return news
