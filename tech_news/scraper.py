import requests
import time
from parsel import Selector

# path = "https://www.tecmundo.com.br/novidades"
# path = (
#     "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/"
#     "155000-musk-tesla-carros-totalmente-autonomos.htm"
# )
# path = (
#     "https://www.tecmundo.com.br/dispositivos-moveis/"
#     "215327-pixel-5a-tera-lancamento-limitado-devido-escassez-chips.htm"
# )
# path = (
#     "https://www.tecmundo.com.br/minha-serie/"
#     "215168-10-viloes-animes-extremamente-inteligentes.htm"
# )


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(url, timeout=3)
        if res.status_code == 200:
            return res.text

        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    list_urls = selector.css("h3.tec--card__title a::attr(href)").getall()

    return list_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    try:
        return selector.css("a.tec--btn ::attr(href)").get()
    except requests.Timeout:
        None


def get_shares_count(selector):
    shares_count = selector.xpath(
        '//div[contains(@class, "tec--toolbar__item")]/text()'
    ).get()
    if shares_count:
        shares_count = shares_count.split()[0]
    else:
        shares_count = 0
    return shares_count


def get_writer(selector):
    writer = selector.css(".z--font-bold ::text").get()
    writer = writer.strip() if writer else None
    return writer


def get_sources(selector):
    sources = selector.css(".z--mb-16 .tec--badge::text")
    _sources = []
    for source in sources.getall():
        _sources.append((source).strip())
    return _sources


def get_categories(selector):
    categories = selector.xpath(
        '//div[contains(@id, "js-categories")]/* /text()'
    )
    _categories = []
    for category in categories.getall():
        _categories.append((category).strip())
    return _categories


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    _url = selector.xpath('//link[contains(@rel, "canonical")]/@href')
    _title = selector.xpath('//h1[contains(@id, "js-article-title")]/text()')
    _timestamp = selector.xpath(
        '//time[contains(@id, "js-article-date")]/@datetime'
    )
    _comments_count = selector.xpath(
        '//button[contains(@class, "tec--btn")]/@data-count'
    )
    _summary = selector.xpath(
        '//div[contains(@class, "tec--article__body")]'
        "/p[1]/descendant-or-self::* /text()"
    )

    return {
        "url": _url.get(),
        "title": _title.get(),
        "timestamp": _timestamp.get(),
        "writer": get_writer(selector),
        "shares_count": int(get_shares_count(selector)),
        "comments_count": int(_comments_count.get()),
        "summary": "".join(_summary.getall()),
        "sources": get_sources(selector),
        "categories": get_categories(selector),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    pass
