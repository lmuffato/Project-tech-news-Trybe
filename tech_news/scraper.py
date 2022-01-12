import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url)
        if (response.status_code == 200):
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    url_list = []
    for notice in selector.css("div.tec--list__item"):
        url = notice.css("a.tec--card__title__link::attr(href)").get()
        url_list.append(url)
    return url_list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    next_page_url = selector.css("a.tec--btn::attr(href)").get()
    if next_page_url:
        return next_page_url
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    url = selector.css('head link[rel=canonical]::attr(href)').get()

    title = selector.css('h1.tec--article__header__title::text').get()

    datetime = selector.css(
        'div.tec--timestamp__item time::attr(datetime)'
    ).get()

    writer = selector.css('.z--font-bold *::text').get()
    if writer:
        writer = writer.strip()

    share_count = selector.css('div.tec--toolbar__item::text').get()
    if share_count:
        share_count = int(share_count.strip()[0])
    else:
        share_count = 0
    comment_count = selector.css('#js-comments-btn::attr(data-count)').get()

    summary = ''.join(selector.css(
        'div.tec--article__body > p:nth-child(1) *::text'
    ).getall())

    sources = selector.css('div.z--mb-16 .tec--badge::text').getall()
    format_sources = [
        i.strip()
        for i in sources
    ]

    categories = selector.css('#js-categories a *::text').getall()
    format_category = [
        i.strip()
        for i in categories
    ]

    body_notice = {
        "url": url,
        "title": title,
        "timestamp": datetime,
        "writer": writer,
        "shares_count": share_count,
        "comments_count": int(comment_count),
        "summary": summary,
        "sources": format_sources,
        "categories": format_category,
    }
    return body_notice


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    new_list_urls = []
    page_html = fetch('https://www.tecmundo.com.br/novidades')

    new_list_urls.extend(scrape_novidades(page_html))

    while len(new_list_urls) < amount:
        link_next_page = scrape_next_page_link(page_html)
        next_page = fetch(link_next_page)
        new_list_urls.extend(scrape_novidades(next_page))
    result = []

    for url in new_list_urls[:amount]:
        page = fetch(url)
        result.append(scrape_noticia(page))
    create_news(result)
    return result
