import requests
import time
import parsel


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(url, timeout=3)
        if res.status_code == 200:
            return res.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    list = []
    for news in selector.css("h3.tec--card__title a::attr(href)").getall():
        list.append(news)
    return list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    btn = selector.css("a.tec--btn::attr(href)").get()
    if btn:
        return btn
    else:
        return None


# Requisito 4

def get_all_categories(selector):
    categories = []
    get_categories = selector.css("div#js-categories a::text").getall()
    for element in get_categories:
        categories.append(element.strip())
    return categories


def get_writer(selector):
    method01 = selector.css(".tec--timestamp__item a::text").get()
    method02 = selector.css("a.tec--author__info__link::text").get()
    method03 = selector.css(".tec--author__info > p:first-child::text").get()
    if method01 is not None:
        writer_article = method01.strip()
        return writer_article
    elif method02 is not None:
        writer_article = method02.strip()
        return writer_article
    elif method03 is not None:
        writer_article = method03.strip()
        return writer_article
    else:
        return None


def get_all_sources(selector):
    sources = []
    get_sources = selector.css("div.z--mb-16 a::text").getall()

    for source in get_sources:
        sources.append(source.strip())

    return sources


def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    notes = {}
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    date = selector.css("time#js-article-date::attr(datetime)").get()
    writer = get_writer(selector)
    shares = selector.css("div.tec--toolbar__item::text").re_first(r"\d+")
    share_note = int(shares) if shares else 0
    comments = int(selector.css("button.tec--btn::attr(data-count)").get())
    summary = "".join(
        selector.css(
            "div.tec--article__body > p:first-child *::text").getall()
    )
    sources = get_all_sources(selector)
    categories = get_all_categories(selector)

    notes.update(url=url, title=title, timestamp=date, writer=writer,
                 shares_count=share_note, comments_count=comments,
                 summary=summary, sources=sources, categories=categories)
    return notes


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
