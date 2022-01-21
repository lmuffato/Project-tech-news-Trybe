import requests
from time import sleep
from parsel import Selector
from tech_news.database import create_news


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


def scrape_summary_in_noticia(document):
    try:
        summary = "".join(
            (
                Selector(
                    text=document.css(
                        ".tec--article__body.p402_premium p:first-child"
                    ).getall()[0]
                )
                .css("p *::text")
                .getall()
            )
        )

        return summary
    except IndexError:
        summary = "".join(
            document.css(
                ".tec--article__body.z--px-16 p:first-child *::text"
            ).getall()
        )

        return summary


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

    comments_count = document.css("#js-comments-btn::attr(data-count)").get()
    if comments_count is not None:
        comments_count = int(comments_count)
    elif comments_count is None:
        comments_count = 0

    summary = "".join(
        document.css(
            ".tec--article__body.p402_premium p:first-child *::text"
        ).getall()
    )

    summary = scrape_summary_in_noticia(document)

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
    document = fetch("https://www.tecmundo.com.br/novidades")
    news = scrape_novidades(document)
    length_news = len(news)
    while length_news < amount:
        next_page = scrape_next_page_link(document)
        document = fetch(next_page)
        more_news = scrape_novidades(document)
        for new in more_news:
            news.append(new)
            length_news += 1

    amount_news = list(news[index] for index in range(amount))
    data = list(scrape_noticia(fetch(new)) for new in amount_news)
    create_news(data)
    return data
