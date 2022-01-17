import requests
import time
import parsel


# Requisito 1


def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    if response.status_code and response.status_code == 200:
        return response.text
    return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    class_name = ".tec--list__item  .tec--card__title__link::attr(href)"
    return selector.css(class_name).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    return selector.css(".tec--btn::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    notice_selector = parsel.Selector(html_content)
    link = notice_selector.css("head link[rel=canonical]::attr(href)").get()
    title = notice_selector.css(".tec--article__header__title::text").get()
    timestamp = notice_selector.css("#js-article-date::attr(datetime)").get()
    writer = (notice_selector.css(".tec--author__info__link::text").get()
    or notice_selector.css(".tec--timestamp__item.z--font-bold > a::text").get()
    or notice_selector.css(".z--m-none.z--truncate.z--font-bold::text").get()
    or None)
    if writer:
        writer = writer.strip()
    shares_count = notice_selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    comments_count = notice_selector.css("#js-comments-btn::text").re_first(r"\d+")
    if comments_count == None:
        comments_count = 0
    else:
        comments_count = int(comments_count)
    if shares_count == None:
        shares_count = 0
    else:
        shares_count = int(shares_count)
    sources = notice_selector.css(".z--mb-16 .tec--badge::text").getall()
    formated_sources = []
    for source in sources:
        formated_source = source.strip()
        formated_sources.append(formated_source)
    summary = notice_selector.css("div.tec--article__body p:nth-child(1) *::text").getall()

    formated_summary = ''.join(summary)
    categories = notice_selector.css("#js-categories a::text").getall()
    formated_categories = []
    for categorie in categories:
        formated_categorie = categorie.strip(" ")
        formated_categories.append(formated_categorie)
    return {
        "url": link,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": formated_summary,
        "sources": formated_sources,
        "categories": formated_categories,
    }

# fonte de consulta para o método strip: https://www.tutorialspoint.com/python3/string_strip.htm

# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

    #js-main > div > article > div.tec--article__body-grid > div.z--pt-40.z--pb-24 >
    # div.z--flex.z--items-center > div.tec--timestamp.tec--timestamp--lg >
