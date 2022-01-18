import time
import requests
import parsel


# Requisito 1
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


# Requisito 2
def scrape_novidades(html_content):
    html_code = parsel.Selector(html_content)
    links = []

    for index in html_code.css("h3.tec--card__title"):
        news = index.css("a.tec--card__title__link::attr(href)").get()
        links.append(news)

    return links


# Requisito 3
def scrape_next_page_link(html_content):
    html_code = parsel.Selector(html_content)
    btn = html_code.css("a.tec--btn::attr(href)").get()

    if btn:
        return btn
    else:
        return None


# Requisito 4
def categories_list(html_code):
    categories = []
    search_categories = html_code.css("div#js-categories a::text").getall()
    for search in search_categories:
        categories.append(search.strip())
    return categories


def writer_selector(html_code):
    way01 = html_code.css(".tec--timestamp__item a::text").get()
    way02 = html_code.css("a.tec--author__info__link::text").get()
    way03 = html_code.css(".tec--author__info > p:first-child::text").get()
    if way01 is not None:
        writer = way01.strip()
        return writer
    elif way02 is not None:
        writer = way02.strip()
        return writer
    elif way03 is not None:
        writer = way03.strip()
        return writer
    else:
        return None


def info_source(html_code):
    list_source = []
    search_source = html_code.css("div.z--mb-16 a::text").getall()

    for source in search_source:
        list_source.append(source.strip())

    return list_source


def scrape_noticia(html_content):
    html_code = parsel.Selector(html_content)
    info = {}
    url = html_code.css("head link[rel=canonical]::attr(href)").get()
    title = html_code.css("h1.tec--article__header__title::text").get()
    timestamp = html_code.css("time#js-article-date::attr(datetime)").get()
    writer = writer_selector(html_code)
    shares = html_code.css("div.tec--toolbar__item::text").re_first(r"\d+")
    users_shares = int(shares) if shares else 0
    comments = int(html_code.css("button.tec--btn::attr(data-count)").get())
    summary = "".join(
        html_code.css(
            "div.tec--article__body > p:first-child *::text").getall()
    )
    sources = info_source(html_code)
    categories = categories_list(html_code)

    info.update(url=url, title=title, timestamp=timestamp, writer=writer)
    info.update(shares_count=users_shares, comments_count=comments)
    info.update(summary=summary, sources=sources, categories=categories)
    return info


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
