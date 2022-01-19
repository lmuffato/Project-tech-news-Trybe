from tech_news.database import create_news
from parsel import Selector
import requests
import time
import re


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

    links = selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()

    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)

    next_page = selector.css("a.tec--btn::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    get_writer = selector.css(".z--font-bold ::text").get()
    if not get_writer:
        writer = None
    else:
        writer = get_writer.strip()

    get_shares = selector.css(
        "article.tec--article div.tec--toolbar__item::text").get()
    if not get_shares:
        shares_count = 0
    else:
        shares_count = int(re.findall('[0-9]+', get_shares)[0])

    get_comments = selector.css("button#js-comments-btn::text").getall()[1]
    if not get_comments:
        comments_count = 0
    else:
        comments_count = int(re.findall('[0-9]+', get_comments)[0])

    get_summary = selector.css(
      "article.tec--article div.tec--article__body > p:first_child *::text"
      ).getall()
    summary = "".join(get_summary).strip()

    news_item = dict({
        "url": selector.css("meta[property='og:url']::attr(content)").get(),
        "title": selector.css("h1.tec--article__header__title::text").get(),
        "timestamp": selector.css(
            "div.tec--timestamp__item time::attr(datetime)").get(),
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": [source.strip() for source in selector.css(
            "article.tec--article div.z--mb-16 a.tec--badge::text"
        ).getall()],
        "categories": [category.strip() for category in selector.css(
            "#js-categories a::text"
        ).getall()]
    })

    return news_item

    # Referências para fazer requisito 4:
    # https://github.com/tryber/sd-010-a-tech-news/pull/17/commits/1188328a1ec8e1428cf364b6cd3dafc61f1a0d74
    # https://www.guru99.com/python-regular-expressions-complete-tutorial.html


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    content = fetch(url)
    latest_news = scrape_novidades(content)
    tech_news_list = []

    while len(latest_news) < amount:
        url = scrape_next_page_link(content)
        content = fetch(url)
        latest_news.extend(scrape_novidades(content))

    for url_news in latest_news:
        if len(tech_news_list) < amount:
            new_news = fetch(url_news)
            scraped_news = scrape_noticia(new_news)
            tech_news_list.append(scraped_news)

    create_news(tech_news_list)
    return tech_news_list
