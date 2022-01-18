import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):

    try:
        res = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if res.status_code == 200:
        return res.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    res = Selector(html_content)
    res_links = res.css(
        "div.tec--list__item > article > div > h3 > a::attr(href)"
    ).getall()
    return res_links


# Requisito 3
def scrape_next_page_link(html_content):

    res = Selector(html_content)
    res_next_page = res.css(
        "div.z--col.z--w-2-3 > div.tec--list.tec--list--lg > a ::attr(href)"
    ).get()
    return res_next_page


# Requisito 4
def get_all_categories(page_code):
    categories = []
    get_categories = page_code.css("div#js-categories a::text").getall()
    for element in get_categories:
        categories.append(element.strip())
    return categories


def get_writer(page_code):
    tecnote1 = page_code.css(".tec--timestamp__item a::text").get()
    tecnote2 = page_code.css("a.tec--author__info__link::text").get()
    tecnote3 = page_code.css(".tec--author__info > p:first-child::text").get()
    if tecnote1 is not None:
        writer_article = tecnote1.strip()
        return writer_article
    elif tecnote2 is not None:
        writer_article = tecnote2.strip()
        return writer_article
    elif tecnote3 is not None:
        writer_article = tecnote3.strip()
        return writer_article
    else:
        return None


def get_all_sources(page_code):
    sources = []
    get_sources = page_code.css("div.z--mb-16 a::text").getall()

    for source in get_sources:
        sources.append(source.strip())

    return sources


def scrape_noticia(html_content):
    page_code = Selector(html_content)
    notes = {}
    url = page_code.css("head link[rel=canonical]::attr(href)").get()
    title = page_code.css("h1.tec--article__header__title::text").get()
    date = page_code.css("time#js-article-date::attr(datetime)").get()
    writer = get_writer(page_code)
    shares = page_code.css("div.tec--toolbar__item::text").re_first(r"\d+")
    share_note = int(shares) if shares else 0
    comments = int(page_code.css("button.tec--btn::attr(data-count)").get())
    summary = "".join(
        page_code.css(
            "div.tec--article__body > p:first-child *::text").getall()
    )
    sources = get_all_sources(page_code)
    categories = get_all_categories(page_code)

    notes.update(url=url, title=title, timestamp=date, writer=writer)
    notes.update(shares_count=share_note, comments_count=comments)
    notes.update(summary=summary, sources=sources, categories=categories)
    return notes


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
