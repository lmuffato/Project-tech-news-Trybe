import requests
import time
import parsel
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    return {
        "url": selector.css("head link[rel=canonical]::attr(href)").get(),
        "title": selector.css("#js-article-title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": autores(selector),
        "shares_count": compartilhamentos(selector),
        "comments_count": comentarios(selector),
        "summary": resumo(selector),
        "sources": [fonte.strip() for fonte in selector.css(
            ".z--mb-16 .tec--badge::text"
        ).getall()],
        "categories": [categoria.strip() for categoria in selector.css(
            "#js-categories a::text"
        ).getall()],
    }


def autores(selector):
    autor = selector.css('.z--font-bold *::text').get()

    return autor.strip() if autor else None


def compartilhamentos(selector):
    try:
        return int(
            selector
            .css('.tec--toolbar__item::text')
            .get()
            .strip()[0]
        )
    except (AttributeError, TypeError):
        return 0


def comentarios(selector):
    try:
        return int(
            selector
            .css('#js-comments-btn::attr(data-count)')
            .get()
        )
    except (AttributeError, TypeError):
        return 0


def resumo(selector):
    return "".join(
        selector
        .css('.tec--article__body > p:first-of-type *::text')
        .getall())


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selec = parsel.Selector(text=html_content)
    return selec.css(".tec--list .tec--card__title__link::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(text=html_content)
    return selector.css(".tec--btn::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    Selected = []
    getUrl = "https://www.tecmundo.com.br/novidades"

    while len(Selected) < amount:
        html_content = fetch(getUrl)
        novidades = scrape_novidades(html_content)
        for link in novidades:
            link_content = fetch(link)
            noticia = scrape_noticia(link_content)
            Selected.append(noticia)
            if len(Selected) == amount:
                break

        getUrl = scrape_next_page_link(html_content)

    create_news(Selected)
    return Selected
