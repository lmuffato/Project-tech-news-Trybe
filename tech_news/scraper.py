import time
import requests
import parsel


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        html = requests.get(url, timeout=3)

        if html.status_code == 200:
            return html.text
        return None

    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)

    links = [
        cardTitle.css("a.tec--card__title__link::attr(href)").get()
        for cardTitle in selector.css("h3.tec--card__title")
    ]
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    nextLinkPage = selector.css("a.tec--btn::attr(href)").get()

    if nextLinkPage:
        return nextLinkPage
    return None


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)

    url = selector.css("head link[rel=canonical]::attr(href)").get()

    title = selector.css(".tec--article__header__title::text").get()

    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    writer = selector.css(".z--font-bold *::text").get()
    writer = writer.strip() if writer else None

    shares_count = selector.css(".tec--toolbar__item::text").get()
    shares_count = shares_count.strip().split(" ")[0] if shares_count else 0

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    comments_count = comments_count if comments_count else 0

    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    summary = "".join(summary)

    sources = [
        source.strip()
        for source in selector.css(".z--mb-16 div a::text").getall()
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
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
