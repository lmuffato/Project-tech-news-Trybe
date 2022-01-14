import requests
import time
import parsel
# import math
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    links = []
    for new in selector.css("div.tec--list__item"):
        link = new.css("a.tec--card__title__link::attr(href)").get()
        links.append(
            link,
        )
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    try:
        next_page_link = selector.css("a.tec--btn--lg::attr(href)").get()
        return next_page_link
    except requests.Timeout:
        return None


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    url = selector.xpath('//link[contains(@rel, "canonical")]/@href').get()
    title = selector.css("h1#js-article-title::text").get()
    timestamp = selector.xpath('//time/@datetime').get()

    writer = selector.css('.z--font-bold ::text').get()
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
        selector.css('.tec--article__body > p:first_child *::text').getall()
        ).strip()

    sources = []
    getSources = selector.css('.z--mb-16 .tec--badge::text').getall()
    for source in getSources:
        sources.append(source.strip())

    categories = []
    getCategories = selector.css('#js-categories a::text').getall()
    for categorie in getCategories:
        categories.append(categorie.strip())

    data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count":
            comments_count if comments_count is None
            else (int(comments_count)),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }
    return(data)


# Requisito 5
def get_tech_news(amount):
    page_url = 'https://www.tecmundo.com.br/novidades'
    news_urls = []
    news_content = []

    def get_news_urls(page_url):
        html_content = fetch(page_url)
        news_urls.extend(scrape_novidades(html_content))

    while(len(news_urls) < amount):
        get_news_urls(page_url)
        html_content = fetch(page_url)
        page_url = scrape_next_page_link(html_content)

    for new_url in news_urls[0:amount]:
        new_data = fetch(new_url)
        scraped_new = scrape_noticia(new_data)
        news_content.append(scraped_new)
    create_news(news_content)
    return(news_content)
