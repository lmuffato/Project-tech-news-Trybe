from parsel import Selector
import requests
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    href = selector.css(".tec--card__info h3 a::attr(href)").getall()
    return href


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(".tec--list--lg > a::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css('head link[rel="canonical"]::attr(href)').get()
    title = selector.css(".tec--article h1::text").get()
    timestamp = selector.css(".tec--article time::attr(datetime)").get()
    writer_name = selector.css(".z--font-bold *::text").get()

    if writer_name:
        writer = writer_name.strip()
    else:
        writer = None

    shares_count = selector.css(
        "div.tec--toolbar__item::text"
    ).re_first(r"[0-9]")
    if not shares_count:
        shares_count = 0

    comments_count = selector.css(
        "button#js-comments-btn::attr(data-count)"
    ).get()
    if not comments_count:
        comments_count = 0

    summary_text = selector.css(
        "div.tec--article__body > p:first-child *::text"
    ).getall()
    summary = "".join(summary_text).strip()

    sources_list = selector.css(
        "div.z--mb-16 a.tec--badge::text"
    ).getall()
    sources = [source.strip() for source in sources_list]

    categories_list = selector.css(
        "div#js-categories a.tec--badge::text"
    ).getall()
    categories = [category.strip() for category in categories_list]

    result = dict({
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories
    })
    return result


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"

    links_list = []
    while len(links_list) < amount:
        html_content = fetch(url)
        links_list.extend(scrape_novidades(html_content))
        url = scrape_next_page_link(html_content)

    news_list = []
    index = 0
    while len(news_list) < amount:
        html_content = fetch(links_list[index])
        news = scrape_noticia(html_content)
        news_list.append(news)
        index += 1

    create_news(news_list)
    return news_list
