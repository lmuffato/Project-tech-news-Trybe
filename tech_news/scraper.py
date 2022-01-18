import time
import requests
import parsel
from tech_news.database import create_news

AUTHOR = ".z--font-bold ::text"

URL = "head > link[rel=canonical]::attr(href)"

TITLE = "#js-article-title::text"

TIMESTAMP = "#js-article-date::attr(datetime)"

SRC = ".z--mb-16 .tec--badge::text"

CATEGORIE = "#js-categories a::text"

BAR_AUTHOR = "#js-author-bar > nav > div:nth-child(1)::text"

COMMENTS = "#js-comments-btn::attr(data-count)"

SUMMARY = ".tec--article__body > p:first_child *::text"


def fetch(url):
    try:
        time.sleep(1)
        request = requests.get(url, timeout=3)
        if request.status_code == 200:
            return request.text
        else:
            return None
    except requests.Timeout:
        return None


def scrape_novidades(html_content):
    content = parsel.Selector(html_content)
    list_url = []

    for url in content.css("h3.tec--card__title"):
        reports = url.css("a.tec--card__title__link::attr(href)").get()
        list_url.append(reports)

    return list_url


def scrape_next_page_link(html_content):
    content = parsel.Selector(html_content)
    btn = content.css("a.tec--btn::attr(href)").get()

    if btn:
        return btn
    else:
        return None


def scrape_noticia(html_content):
    selector = parsel.Selector(text=html_content)

    url = selector.css(URL).get()

    title = selector.css(TITLE).get()

    timestamp = selector.css(TIMESTAMP).get()

    writer = selector.css(AUTHOR).get()

    if writer:
        writer = writer.strip()
    else:
        writer = None

    sources = [source.strip() for source in selector.css(SRC).getall()]

    categories = [
        category.strip() for category in selector.css(CATEGORIE).getall()
    ]

    shares_count = selector.css(BAR_AUTHOR).get()

    if shares_count:
        shares_count = shares_count.split()[0]
    else:
        shares_count = 0

    comments_count = selector.css(COMMENTS).get()

    summary = "".join(selector.css(SUMMARY).getall())

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "sources": sources,
        "categories": categories,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
    }


# Requisito 5 com ajuda do Daniel Ribeiro T10A
def get_tech_news(amount):
    checker = 0
    URL = "https://www.tecmundo.com.br/novidades"
    infos = []

    while checker < amount:
        link = fetch(URL)
        content = scrape_novidades(link)
        for new in content:
            infos.append(scrape_noticia(fetch(new)))
            checker += 1
            if checker % 10 == 0:
                URL = scrape_next_page_link(link)
            if checker == amount:
                break

    create_news(infos)
    return infos
