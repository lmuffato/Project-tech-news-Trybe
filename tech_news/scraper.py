import time
import requests
import parsel
import re


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    listLinks = []

    for link in selector.css("h3.tec--card__title"):
        noticia = link.css("a.tec--card__title__link::attr(href)").get()
        listLinks.append(noticia)
    return listLinks


def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    buttonNext = selector.css("a.tec--btn::attr(href)").get()
    if buttonNext:
        return buttonNext
    else:
        return None


def vral(selector):
    texto = selector.css('.tec--toolbar__item::text')
    if len(texto) == 0:
        return 0
    else:
        numberTexto = re.findall(r"\d+", texto.get())[0]
        return int(numberTexto)


def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    count_shares = vral(selector)
    try:
        writer = selector.css('.z--font-bold').css('*::text').get().strip()
    except AttributeError:
        writer = ''
    try:
        count_comments = int(selector.css(
            '#js-comments-btn::attr(data-count)'
        ).get())
    except TypeError:
        count_comments = 0
    text = ''.join(
        selector.css('.tec--article__body > p:nth-child(1) ::text').getall()
    )
    cat = selector.css('.tec--badge--primary ::text').getall()
    fon = selector.css('.z--mb-16 .tec--badge ::text').getall()

    return {
        "url": selector.css('link[rel=canonical]::attr(href)').get(),
        "title": selector.css('.tec--article__header__title::text').get(),
        "timestamp": selector.css('time::attr(datetime)').get(),
        "writer": writer,
        "shares_count": count_shares,
        "comments_count": count_comments,
        "summary": text,
        "sources": [font.strip() for font in fon],
        "categories": [categoria.strip() for categoria in cat]
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
