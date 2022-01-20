import requests
import time
from parsel import Selector
from .database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        return response.text if response.status_code == 200 else None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(
        'h3.tec--card__title a.tec--card__title__link::attr(href)'
        ).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link = selector.css(
        'a.tec--btn::attr(href)'
        ).getall()
    return link[0] if link else None


# Requisito 4
def scrape_noticia(html_content):
    noticias = {}
    selector = Selector(text=html_content)
    url = selector.css(
            'head link[rel=canonical]::attr(href)'
            ).get()
    noticias['url'] = url
    title = selector.css(
            'h1.tec--article__header__title::text'
            ).get()
    noticias['title'] = title
    timestamp = selector.css(
            'time::attr(datetime)'
            ).get()
    noticias['timestamp'] = timestamp
    writer = selector.css(
            '.z--font-bold *::text'
            ).get()
    noticias['writer'] = writer.strip() if writer else None
    shares_count = selector.css(
            'div.tec--toolbar__item::text'
            ).re_first(r"\d+")
    noticias['shares_count'] = int(shares_count) if shares_count else 0
    comments_count = selector.css(
            '#js-comments-btn::attr(data-count)'
            ).get()
    noticias['comments_count'] = int(comments_count)
    summary = "".join(selector.css(
            'div.tec--article__body p:first-child *::text'
            ).getall())
    noticias['summary'] = summary
    sources = selector.css(
        'div.z--mb-16 a::text'
    ).getall()
    sources = [s.strip() for s in sources]
    noticias['sources'] = sources
    categories = selector.css(
        'div#js-categories a.tec--badge::text'
    ).getall()
    categories = [c.strip() for c in categories]
    noticias['categories'] = categories
    return noticias


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(url)
    links = scrape_novidades(html_content)
    while len(links) < amount:
        next_link = scrape_next_page_link(html_content)
        html_content = fetch(next_link)
        links.extend(scrape_novidades(html_content))
    noticias = []
    for link in links[:amount]:
        html_content = fetch(link)
        noticias.append(scrape_noticia(html_content))
    create_news(noticias)
    return noticias
