import time
import requests
import parsel
from .database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        requisition = requests.get(url, timeout=3)

        if requisition.status_code == 200:
            return requisition.text
        else:
            return None

    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    site_content = parsel.Selector(html_content)
    links_news = []
    for link in site_content.css("h3.tec--card__title"):
        new_link = link.css("a.tec--card__title__link::attr(href)").get()
        links_news.append(new_link)
    return links_news


# Requisito 3
def scrape_next_page_link(html_content):
    site_content = parsel.Selector(html_content)
    btn_next_page = site_content.css("a.tec--btn::attr(href)").get()

    if btn_next_page:
        return btn_next_page
    else:
        return None


# Requisito 4
def author_selector(site_content):
    mode1 = site_content.css("a.tec--author__info__link::text").get()
    mode2 = site_content.css(".tec--author__info > p:first-child::text").get()
    mode3 = site_content.css(".tec--timestamp__item a::text").get()
    if mode1 is not None:
        author = mode1.strip()
        return author
    elif mode2 is not None:
        author = mode2.strip()
        return author
    elif mode3 is not None:
        author = mode3.strip()
        return author
    else:
        return None


def source_news(site_content):
    list = []
    search_by_sources = site_content.css("div.z--mb-16 a::text").getall()

    for search in search_by_sources:
        list.append(search.strip())

    return list


def categories_list(site_content):
    categories = []
    search_categories = site_content.css("div#js-categories a::text").getall()

    for search in search_categories:
        categories.append(search.strip())

    return categories


def scrape_noticia(html_content):
    site_content = parsel.Selector(html_content)
    news = {}
    url = site_content.css("head link[rel=canonical]::attr(href)").get()
    title = site_content.css("h1.tec--article__header__title::text").get()
    date = site_content.css("time#js-article-date::attr(datetime)").get()
    author = author_selector(site_content)

    share = site_content.css("div.tec--toolbar__item::text").re_first(r"\d+")
    send_news = int(share) if share else 0

    comments = int(site_content.css("button.tec--btn::attr(data-count)").get())
    summary = "".join(
        site_content.css(
            "div.tec--article__body > p:first-child *::text"
        ).getall()
    )
    sources = source_news(site_content)
    categories = categories_list(site_content)

    news.update(url=url, title=title, timestamp=date, writer=author)
    news.update(shares_count=send_news, comments_count=comments)
    news.update(summary=summary, sources=sources, categories=categories)

    return news


# Requisito 5
def get_tech_news(amount):
    url_news = fetch("https://www.tecmundo.com.br/novidades")
    links_news = scrape_novidades(url_news)

    while len(links_news) < amount:
        next_page = scrape_next_page_link(url_news)
        news_next_page = fetch(next_page)
        links_news.extend(scrape_novidades(news_next_page))

    news = []
    for link in links_news[:amount]:
        new_site_content = fetch(link)
        other_news = scrape_noticia(new_site_content)
        news.append(other_news)

    create_news(news)
    return news
