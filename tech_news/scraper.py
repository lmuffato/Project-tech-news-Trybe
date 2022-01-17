from parsel import Selector
import requests
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui - Iniciando - commit 1"""
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    links = []
    for link in selector.css(".tec--card__info h3"):
        # print(link.css("a::attr(href)").get())
        get_links = link.css("a::attr(href)").get()
        links.append(get_links)
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    next_url_page = selector.css("a.tec--btn::attr(href)").get()
    if next_url_page is not None:
        return next_url_page
    else:
        return None


def find_writer(selector):
    aux_writer = selector.css(".z--font-bold *::text").get()
    if aux_writer:
        return aux_writer.strip()
    else:
        return None


def find_shares_count(selector):
    aux_shares_count = selector.css(".tec--toolbar__item::text").get()
    if aux_shares_count is None:
        return 0
    else:
        return aux_shares_count[:2]


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    aux_selector = selector.css("link")
    for link in aux_selector:
        if link.css("link[rel=canonical]").get():
            url = link.css("link::attr(href)").get()

    title = selector.css("#js-article-title::text").get()

    timestamp = selector.css("time::attr(datetime)").get()

    writer = find_writer(selector)

    shares_count = find_shares_count(selector)

    comments_count = selector.css("button::attr(data-count)").get()

    # https://devhints.io/css
    # https://pt.stackoverflow.com/questions/324979/como-concatenar-itens-de-uma-lista-em-python

    aux_summary = selector.css(
        "div.tec--article__body > p:first-child *::text"
    )
    summary = ''.join(aux_summary.getall())

    sources = []
    for source in selector.css(".z--mb-16 .tec--badge::text").getall():
        sources.append(source.strip())

    categories = []
    for category in selector.css(
        "#js-categories a::text"
    ).getall():
        categories.append(category.strip())

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip(),
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = "https://www.tecmundo.com.br/novidades"
    data = []
    count = 0

    # https://www.w3schools.com/python/ref_func_len.asp
    while count < amount:
        get_html_content = fetch(url)
        get_scrape_novidades = scrape_novidades(get_html_content)

        for link in get_scrape_novidades:
            data.append(scrape_noticia(fetch(link)))
            count += 1
            if count == amount:
                break
        url = scrape_next_page_link(get_html_content)

    create_news(data)
    return data
