import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    sleep(1)

    try:
        html = requests.get(url, timeout=3)

        response = {"status": html.status_code, "document": html.text}

        if response["status"] == 200:
            return response["document"]

        else:
            return None

    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    document = Selector(text=html_content)
    url_news = document.css(".tec--card__info h3 a::attr(href)").getall()

    return url_news


# Requisito 3
def scrape_next_page_link(html_content):
    document = Selector(text=html_content)
    url_to_next_page = document.css(
        ".z--col.z--w-2-3 .tec--list.tec--list--lg div + a::attr(href)"
    ).get()

    return url_to_next_page


# Requisito 4
def scrape_noticia(html_content):
    document = Selector(text=html_content)

    url = document.css("head link[rel=canonical]::attr(href)").get()

    title = document.css("#js-article-title::text").get()

    timestamp = document.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()

    writer = (
        document.css(".tec--timestamp__item.z--font-bold a::text").get()
        or document.css(".z--m-none.z--truncate.z--font-bold a::text").get()
        or document.css(
            ".tec--author__info.z--min-w-none.z--flex.z--flex-col p::text"
        ).get()
    )

    if writer is not None:
        writer = writer.strip()

    shares_count = document.css(".tec--toolbar__item::text").get() or 0

    if shares_count != 0:
        shares_count = int(shares_count.split()[0])

    comments_count = int(
        document.css("#js-comments-btn::attr(data-count)").get()
    )

    summary = "".join(
        document.css(
            ".tec--article__body.p402_premium p:first-child *::text"
        ).getall()
    )

    sources = [
        source.strip()
        for source in document.css(
            ".z--mb-16 h2 + div .tec--badge::text"
        ).getall()
    ]

    categories = [
        categorie.strip()
        for categorie in document.css("#js-categories a::text").getall()
    ]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""  # Meu código vai aonde eu quiser parceiro
