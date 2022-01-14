import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        # recurso demora muito a responder
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        # vamos fazer uma nova requisição
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    list = []
    selector = Selector(text=html_content)

    for url in selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall():
        list.append(url)

    return list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_url = selector.css("div.tec--list a.tec--btn::attr(href)").getall()
    if next_url:
        return next_url[0]
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    url = selector.css('meta[property="og:url"]::attr(content)').get()

    title = selector.css("h1#js-article-title::text").get()

    timestamp = selector.css(
            ".tec--timestamp__item time::attr(datetime)"
        ).get()

    writer = selector.css('.z--font-bold ::text').get()
    if writer:
        writer = writer.strip()
    else:
        writer = None

    shares = selector.css('.tec--toolbar__item::text').get()
    if shares:
        shares_count = shares.split()[0]
    else:
        shares_count = 0

    comments_count = selector.css('#js-comments-btn::attr(data-count)').get()
    summary = "".join(
        selector.css('.tec--article__body > p:first_child *::text').getall()
        ).strip()

    sources = []
    source = selector.css('.z--mb-16 .tec--badge::text').getall()
    for s in source:
        sources.append(s.strip())

    categories = []
    category = selector.css('#js-categories a::text').getall()
    for categorie in category:
        categories.append(categorie.strip())

    data = {
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
    return(data)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""