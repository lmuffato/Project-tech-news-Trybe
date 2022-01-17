from tech_news.database import create_news
from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.text

    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    sel = Selector(html_content)
    return sel.css(
        "div.tec--list__item a.tec--card__title__link::attr(href)"
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    sel = Selector(html_content)
    return sel.css("div.z--container a.tec--btn::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    def get_clean_str_list(str_list):
        return [item.strip() for item in str_list]

    sel = Selector(html_content)

    url = sel.css("meta[property='og:url']::attr(content)").get()
    title = sel.css("#js-article-title::text").get()
    timestamp = sel.css("#js-article-date::attr(datetime)").get()
    writer = (
        sel.css("a.tec--author__info__link::text").get()
        or sel.css(".z--font-bold ::text").get()
    )
    shares_count = sel.css(".tec--toolbar__item::text").get()
    comments_count = sel.css("#js-comments-btn::attr(data-count)").get()
    summary = sel.css(".tec--article__body > p:first-child *::text").getall()
    sources = sel.css(".z--mb-16 .tec--badge::text").getall()
    categories = sel.css("#js-categories a::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip() if writer else None,
        "shares_count": int(shares_count.split()[0]) if shares_count else 0,
        "comments_count": int(comments_count) if comments_count else 0,
        "summary": "".join(summary).strip(),
        "sources": get_clean_str_list(sources),
        "categories": get_clean_str_list(categories),
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"

    def get_news_data_by_urls(urls):
        return [scrape_noticia(fetch(url)) for url in urls[:amount]]

    def get_news(url, news_urls=[]):
        html_content = fetch(url)
        news_urls.extend(scrape_novidades(html_content))

        if len(news_urls) < amount:
            next_url = scrape_next_page_link(html_content)
            return get_news(next_url, news_urls)

        return get_news_data_by_urls(news_urls)

    news = get_news(url)
    create_news(news)
    return news
