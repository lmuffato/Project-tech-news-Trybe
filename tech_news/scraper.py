import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    data = Selector(text=html_content)
    links = data.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    url = selector.css("a.tec--btn--lg ::attr(href)").get()

    return url


def extract_comments(comments):
    if comments is None:
        comments = 0
        return comments
    else:
        comments = int(comments)
        return comments


def extract_paragraph(data):
    graph = data.css("div.tec--article__body > p:first-child *::text").getall()
    phrase_complete = "".join(graph)
    return phrase_complete


def extract_categories(data):
    categories_array = []
    categories = data.css("a.tec--badge--primary ::text").getall()

    for category in categories:
        categories_array.append(category.strip())

    return categories_array


def extract_sources(data):
    sources_array = []
    sources = data.css("div.z--mb-16 a::text").getall()

    for source in sources:
        sources_array.append(source.strip())

    return sources_array


def extract_writer(data):
    if data.css(".tec--author__info__link ::text").get():
        writer = data.css(".tec--author__info__link ::text").get()
        return writer
    if data.css(".tec--timestamp__item a::text").get():
        writer = data.css(".tec--timestamp__item a::text").get()
        return writer
    if data.css(".z--m-none ::text").get():
        writer = data.css(".z--m-none ::text").get()
        return writer


# Requisito 4
def scrape_noticia(html_content):
    data = Selector(html_content)
    url = data.css("head link[rel=canonical] ::attr(href)").get()
    title = data.css("h1.tec--article__header__title ::text").get()
    timestamp = data.css("div.tec--timestamp__item ::attr(datetime)").get()
    writer_tech = extract_writer(data)
    writer = writer_tech.strip() if writer_tech else None
    shares_se = "#js-author-bar > nav > div:nth-child(1)::text"
    shares_tech = data.css(shares_se).re_first(r'\d+')
    shares = int(shares_tech) if shares_tech else 0
    comments = data.css("#js-comments-btn ::text").re_first(r'\d+')
    comments_count = int(comments) if comments else 0
    summary = extract_paragraph(data)
    sources = extract_sources(data)
    categories = extract_categories(data)

    news_json = {
      "url": url,
      "title": title,
      "timestamp": timestamp,
      "writer": writer,
      "shares_count": int(shares),
      "comments_count": comments_count,
      "summary": summary,
      "sources": sources,
      "categories": categories
    }
    return news_json


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
