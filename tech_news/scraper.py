import requests
from requests.exceptions import ReadTimeout
import time
import parsel
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except ReadTimeout:
        return None

    if response.status_code != 200:
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    links = selector.css("h3 > a::attr(href)").getall()
    if len(links) == 0:
        return []
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    next_page_link = selector.css(".tec--btn--primary ::attr(href)").get()
    if next_page_link is None:
        return None
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    url = selector.css("[rel=canonical]::attr(href)").get()
    title = selector.css("h1::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    writer = (
        selector.css(".z--font-bold a::text").get()
        or selector.css(".z--font-bold::text").get()
    )
    if writer is not None:
        writer = writer.strip()

    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count is not None:
        shares_count = shares_count.split()[0]
    else:
        shares_count = 0

    comments_count = (
        selector.css("#js-comments-btn::text").getall()[1].split()[0]
    )
    summary = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    sources = selector.css(".z--mb-16 a *::text").getall()
    sources = [source.strip() for source in sources]
    categories = selector.css("#js-categories a *::text").getall()
    categories = [category.strip() for category in categories]
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    data = []
    initial_page_html = fetch('https://www.tecmundo.com.br/novidades')
    notices_links = scrape_novidades(initial_page_html)

    while len(notices_links) < amount:
        next_page_link = scrape_next_page_link(initial_page_html)
        next_page_content = fetch(next_page_link)
        additional_notices_links = scrape_novidades(next_page_content)
        notices_links += additional_notices_links

    for link in notices_links[:amount]:
        content_page_notice = fetch(link)
        notice_scraped = scrape_noticia(content_page_notice)
        data.append(notice_scraped)

    create_news(data)
    return data
