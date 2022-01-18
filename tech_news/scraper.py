import time
import requests
import parsel
from .database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        fetch_html = requests.get(url, timeout=3)

        if fetch_html.status_code == 200:
            return fetch_html.text
        else:
            return None

    except requests.Timeout:
        return None


# REQUISITO 2
def scrape_novidades(html_content):
    code = parsel.Selector(html_content)
    links = []

    for element in code.css("h3.tec--card__title"):
        fetch_link = element.css("a.tec--card__title__link::attr(href)").get()
        links.append(fetch_link)

    return links


# REQUISITO 3
def scrape_next_page_link(html_content):
    code = parsel.Selector(html_content)
    button = code.css("a.tec--btn::attr(href)").get()

    if button:
        return button
    else:
        return None


# REQUISITO 4
def get_all_categories(page_code):
    categories = []
    get_categories = page_code.css("div#js-categories a::text").getall()
    for element in get_categories:
        categories.append(element.strip())
    return categories


def get_all_sources(page_code):
    sources = []
    get_sources = page_code.css("div.z--mb-16 a::text").getall()

    for source in get_sources:
        sources.append(source.strip())

    return sources


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


def scrape_noticia(html_content):
    page_code = parsel.Selector(html_content)
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


# REQUISITO 5


def get_tech_news(amount):
    url = fetch("https://www.tecmundo.com.br/novidades")
    links = scrape_novidades(url)

    while len(links) < amount:
        more_pages = scrape_next_page_link(url)
        next_page = fetch(more_pages)
        links.extend(scrape_novidades(next_page))

    notes = []
    for element in links[:amount]:
        new_code = fetch(element)
        new_note = scrape_noticia(new_code)
        notes.append(new_note)

    create_news(notes)
    return notes
