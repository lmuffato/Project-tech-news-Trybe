from time import sleep
import requests
from parsel import Selector
from .database import create_news
URL_BASE = 'https://www.tecmundo.com.br/novidades'


# Requisito 1
def fetch(url):
    # """Seu código deve vir aqui"""
    sleep(1)
    # Garante o intervalo de 1 segundo entre cada requisição.
    try:
        html = requests.get(url, timeout=3)
        # Permite http requests usando python
    except requests.Timeout:
        return None
    if html.status_code == 200:
        return html.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    # """Seu código deve vir aqui"""
    selector = Selector(html_content)
    return selector.css(
        'main .tec--card__title__link::attr(href)'
    ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    next_page = selector.css('a.tec--btn::attr(href)').get()
    if next_page == '':
        return None
    else:
        return next_page


# Requisito 4
def scrape_noticia(html_content):
    # """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news_url = selector.css("head link[rel=canonical::attr(href)").get()
    news_title = selector.css(".tec--article__header__title::text").get()
    news_timestamp = selector.css("#js-article-date::attr(datetime)").get()
    author = selector.css(".z--font-bold *::text").get()
    news_author = author.strip() if author else None
    shares_count = selector.css(".tec--toolbar__item::text").get()
    news_shares_count = (
        shares_count.strip().split(" ")[0] if shares_count else 0
    )
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    news_comments_count = comments_count if comments_count else 0
    summary = selector.css(
        ".tec--article__body p:first-child *::text"
    ).getall()
    news_summary = "".join(summary)

    news_sources = []
    for source in selector.css(".z--mb-16 div a::text").getall():
        news_sources.append(source.strip())

    news_categories = []
    for category in selector.css("#js-categories a::text").getall():
        news_categories.append(category.strip())
    return {
        "url": news_url,
        "title": news_title,
        "timestamp": news_timestamp,
        "writer": news_author,
        "shares_count": int(news_shares_count),
        "comments_count": int(news_comments_count),
        "summary": news_summary,
        "sources": news_sources,
        "categories": news_categories,
    }


# Requisito 5
def get_tech_news(amount):
    # """Seu código deve vir aqui"""
    news_list = []
    html = fetch(URL_BASE)

    news_list.extend(scrape_novidades(html))
    while len(news_list) <= amount:
        next_page_link = scrape_next_page_link(html)
        next_page = fetch(next_page_link)
        news_list.extend(scrape_novidades(next_page))

    result = []

    for item in news_list[:amount]:
        page = fetch(item)
        result.append(scrape_noticia(page))

    create_news(result)
    return result
