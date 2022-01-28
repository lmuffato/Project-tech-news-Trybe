import requests
import time
import parsel
from .database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(text=html_content)
    array = []
    if len(array) == 0:
        return selector.css(
            ".tec--list .tec--card__title__link::attr(href)"
        ).getall()
    else:
        return array


def scrape_next_page_link(html_content):
    selector = parsel.Selector(text=html_content)
    next_page_url = selector.css(".tec--btn::attr(href)").get()
    if next_page_url != "":
        return next_page_url
    else:
        return None


def scrape_next_page_exemple(link):
    response = requests.get(link)
    selector = parsel.Selector(text=response.text)
    next_page_url = selector.css(
        ".tec--btn.tec--btn--lg.tec--btn--primary.z--mt-48::attr(href)"
    ).get()
    return next_page_url


# Requisito 4
def find_writer(selector):
    writer = (
        selector.css(".tec--author__info__link ::text").get()
        or selector.css(".tec--timestamp__item.z--font-bold ::text").get()
        or selector.css(".z--m-none.z--truncate.z--font-bold ::text").get()
    )
    if writer:
        writer = writer.strip()
    return writer


def shares_counter(selector):
    shares_count_str = selector.css(".tec--toolbar__item ::text").get().strip()
    if shares_count_str == "":
        shares_count = 0
    else:
        shares_count = int(shares_count_str.split(" ")[0])
    return shares_count


def get_categories(selector):
    categories_list = selector.css("#js-categories ::text").getall()
    categories = []
    for category in categories_list:
        if category != " ":
            categories.append(category.strip())
    return categories


def scrape_noticia(html_content):
    selector = parsel.Selector(text=html_content)
    url = selector.css("head link[rel=canonical] ::attr(href)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    comments_count = selector.css("#js-comments-btn ::attr(data-count)").get()
    if comments_count == "" or None:
        comments_count = 0
    else:
        comments_count = int(comments_count)
    summary_list = selector.css(
        ".tec--article__body > p:first_child *::text"
    ).getall()
    summary = "".join(summary_list)
    sources_list = selector.css(".z--mb-16 .tec--badge ::text").getall()
    sources = []
    for source in sources_list:
        if source != " ":
            sources.append(source.strip())
    scrape_new = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": find_writer(selector),
        "shares_count": shares_counter(selector),
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": get_categories(selector),
    }
    return scrape_new


# Requisito 5
def get_tech_news(amount):
    html_content = fetch("https://www.tecmundo.com.br/novidades")
    news_list = scrape_novidades(html_content)
    result = []
    while len(news_list) < amount:
        nxt_page = scrape_next_page_link(html_content)
        html_content = fetch(nxt_page)
        news_to_include = scrape_novidades(html_content)
        if (amount - len(news_list)) <= len(news_to_include):
            for i in range(amount - len(news_list)):
                news_list.append(news_to_include[i])
    for news in range(amount):
        content = fetch(news_list[news])
        result.append(scrape_noticia(content))
        # print(f'\n{news_list[news]}')
    create_news(result)
    print(result)
    return result


get_tech_news(2)
# def noticia_html_v3():
#     path = (
#         "tests/"
#         "assets/"
#         "tecmundo_pages/"
#         "seguranca|"
#         "215274-pmes-principais-alvos-ataques-ciberneticos.htm."
#         "html"
#     )
#     with open(path) as f:
#         return f.read()


# print(noticia_html_v3())

# # Req.4
# def test_scrape_noticia(noticia_html_v3):
#     assert scrape_noticia(noticia_html_v3) == all_news[0]


# def mocked_fetch(url):
#     """Fake-fetches html from local file caches"""
#     skip = len("https://www.tecmundo.com.br/")
#     file_id = url[skip:].replace("/", "|")
#     path = f"tests/assets/tecmundo_pages/{file_id}.html"
#     with open(path) as cached_html:
#         return cached_html.read()
