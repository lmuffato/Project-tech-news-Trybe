import requests
import time
from parsel import Selector
from tech_news.database import create_news
import re


# Requisito 1
def fetch(url):
    try:
        result = requests.get(url, timeout=3)
        time.sleep(1)
        if result.status_code == 200:
            return result.text
    except (requests.Timeout, ValueError):
        return None


# Requisito 2
def scrape_novidades(html_content):
    select = Selector(text=html_content)
    ref = ".tec--list__item article h3 a.tec--card__title__link::attr(href)"
    return select.css(ref).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    select = Selector(text=html_content)
    link = select.css("a.tec--btn::attr(href)").getall()
    return link[0] if link else None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.xpath('//link[contains(@rel, "canonical")]/@href').get()
    writer = selector.css(".z--font-bold ::text").get()
    if writer:
        writer = writer.strip()
    else:
        writer = None

    shares_str = selector.css("#js-author-bar nav div::text").get()
    if shares_str:
        shares_num = int(re.findall(r"\d+", shares_str)[0])
    else:
        shares_num = 0

    comments = selector.css("#js-comments-btn::attr(data-count)").get()

    sources = []
    for item in selector.css(".z--mb-16 .tec--badge::text").getall():
        sources.append(item.strip())

    categories = []
    for i in selector.css("#js-categories a::text").getall():
        categories.append(i.strip())

    s = selector.css(".tec--article__body > p:nth-child(1) *::text").getall()
    response = {
        "url": url,
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("time::attr(datetime)").get(),
        "writer": writer,
        "shares_count": shares_num,
        "comments_count": int(comments),
        "summary": "".join(s),
        "sources": sources,
        "categories": categories,
    }
    return response


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(url)
    links = scrape_novidades(html_content)
    while len(links) < amount:
        next_link = scrape_next_page_link(html_content)
        html_content = fetch(next_link)
        links.extend(scrape_novidades(html_content))
    list = []
    for link in links[:amount]:
        html_content = fetch(link)
        list.append(scrape_noticia(html_content))
    create_news(list)
    return list
