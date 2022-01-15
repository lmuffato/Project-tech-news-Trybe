from parsel import Selector
import requests
import time
from tech_news.database import create_news

URL = "https://www.tecmundo.com.br/novidades"
# Requisito 1


def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)

        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
# Estes links estão contidos na página Novidades
# (https://www.tecmundo.com.br/novidades)


def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    data = selector.css("h3.tec--card__title a::attr(href)").getall()
    return data


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    url_next = selector.css("a.tec--btn--lg ::attr(href)").get()
    return url_next


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    #  https://docs.scrapy.org/en/latest/topics/selectors.html
    url = selector.xpath('//link[contains(@rel, "canonical")]/@href').get()
    print(url)

    title = selector.css("h1#js-article-title::text").get()

    # TIMESTAMP = Data e Horas
    timestamp = selector.xpath("//time/@datetime").get()

    # WRITER = Autor da notícia
    writer = selector.css(".z--font-bold ::text").get()
    if writer:
        # https://www.w3schools.com/python/ref_string_strip.asp
        writer = writer.strip()
    else:
        writer = None

    # SHARES = Número de compartilhamendo da noticia
    newShares = selector.css(".tec--toolbar__item::text").get()
    if newShares:
        # https://www.w3schools.com/python/ref_string_split.asp
        shares_count = newShares.split()[0]
    else:
        shares_count = 0

    # COMMENTS = Número de comentários
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()

    # SUMMARY =  O primeiro parágrafo da notícia
    summary = "".join(
        selector.css(".tec--article__body > p:first_child *::text").getall()
    ).strip()

    # SOURCES = Lista contendo fontes da notícia
    sources = []
    newSources = selector.css(".z--mb-16 .tec--badge::text").getall()
    for source in newSources:
        sources.append(source.strip())

    categories = []
    newcategories = selector.css("#js-categories a::text").getall()
    for category in newcategories:
        categories.append(category.strip())

    data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": comments_count
        if comments_count is None
        else (int(comments_count)),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }
    return data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    fetchUrl = fetch(URL)
    urls = []
    newUrls = []
    # O .extend()método aumenta o comprimento da lista pelo número de elementos
    # fornecidos ao método, portanto, se você quiser adicionar vários elementos
    #  à lista, poderá usar    # esse método
    urls.extend(scrape_novidades(fetchUrl))

    while len(urls) < amount:
        nextPage = scrape_next_page_link(fetchUrl)
        newPage = fetch(nextPage)
        urls.extend(scrape_novidades(newPage))

    for index in urls[:amount]:
        page = fetch(index)
        newUrls.append(scrape_noticia(page))

    create_news(newUrls)
    return newUrls
