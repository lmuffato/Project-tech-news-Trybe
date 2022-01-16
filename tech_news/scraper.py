import parsel
import requests
import time
import json

from .database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if (response.status_code == 200):
            return response.text
        if (response.status_code != 200):
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    url_list = []
    selector = parsel.Selector(html_content)
    if(html_content == ''):
        return url_list
    script = selector.css(
        'script[type="application/ld+json"] *::text').getall()[1].strip()
    json_object = json.loads(script)
    item_list = json_object['itemListElement']
    for i in item_list:
        url = i['url']
        url_list.append(url)
    return url_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    link = selector.css(
        "a.tec--btn.tec--btn--lg.tec--btn--primary.z--mx-auto.z--mt-48"
        + "::attr(href)"
        ).get()
    if(not link):
        return None
    return link


def get_shares(selector):
    shares = selector.css('div.tec--toolbar__item *::text').get().strip()
    if (len(shares) == 0):
        return 0
    else:
        digit_list = []
        for s in shares.split():
            if(s.isdigit()):
                digit_list.append(s)
        return int(''.join(digit_list))


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    if(html_content == ''):
        return None
    script = (selector.css(
        'script[type="application/ld+json"] *::text'
        ).getall()[1]).strip()
    json_object = json.loads(script)
    url = json_object['mainEntityOfPage']['@id']
    title = json_object['headline'].strip()
    timestamp = json_object['datePublished']
    get_writer = selector.css('a.tec--author__info__link *::text').get()
    if (get_writer is not None):
        writer = get_writer.strip()
    else:
        writer = json_object['author']['name'] or None
    shares_count = get_shares(selector)
    comments = selector.css('div.tec--toolbar__item *::text').getall()[-1]
    comments_list = []
    for s in comments.split():
        if(s.isdigit()):
            comments_list.append(s)
    comments_count = int(''.join(comments_list))
    summary = "".join(selector.css(
        'div.tec--article__body > p:nth-child(1) *::text'
        ).getall())
    sources = selector.css('a[class="tec--badge"] *::text').getall()
    sources = [i.strip() for i in sources]
    sources = [i for i in sources if len(i) > 0]
    categories = selector.css(
        'a[class="tec--badge tec--badge--primary"] *::text'
        ).getall()
    categories = [i.strip() for i in categories]
    return {"url": url, "title": title, "timestamp": timestamp,
            "writer": writer, "shares_count": shares_count,
            "comments_count": comments_count, "summary": summary,
            "sources": sources, "categories": categories}


# Requisito 5
def get_tech_news(amount):
    news_list = []
    tecmundo_url = 'https://www.tecmundo.com.br/novidades'
    while True:
        tecmundo_page = fetch(tecmundo_url)
        url_list = scrape_novidades(tecmundo_page)
        for url in url_list:
            page = fetch(url)
            news = scrape_noticia(page)
            news_list.append(news)
            if (len(news_list) == amount):
                create_news(news_list)
                return news_list
        tecmundo_url = scrape_next_page_link(tecmundo_page)
