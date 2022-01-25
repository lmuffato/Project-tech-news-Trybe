import time
import requests
import parsel


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None

    if response.status_code != 200:
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    list = []
    selector = parsel.Selector(text=html_content)
    list = selector.css('main .tec--card__title__link::attr(href)').getall()

    return list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(text=html_content)
    next_page = selector.css(".tec--btn::attr(href)").get()

    return next_page if next_page else None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)

    url = selector.css("head link[rel=canonical]::attr(href)").get()

    title = selector.css("#js-article-title::text").get()

    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()

    writer = selector.css(".z--font-bold *::text").get()

    writer = writer.strip() if writer else None

    shares_count = selector.css(".tec--toolbar__item::text").get()

    if shares_count:
        shares_count = int(shares_count.split()[0])
    else:
        shares_count = 0

    comments = selector.css("#js-comments-btn::attr(data-count)").get()

    summary = "".join(
        selector.css(".tec--article__body > p:nth-child(1) *::text").getall()
    )

    sources = [
        source.strip()
        for source in selector.css(
            ".z--mb-16 .tec--badge::text"
        ).getall()
    ]

    categories = [
        category.strip()
        for category in selector.css("#js-categories a::text").getall()
    ]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": int(comments),
        "summary": summary,
        "categories": categories,
        "sources": sources,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
