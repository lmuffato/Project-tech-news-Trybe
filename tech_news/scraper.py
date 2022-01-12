import requests
import time

from parsel import Selector


# Requisito 1
def fetch(url):
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
def scrape_novidades(html_content):
    selector = Selector(html_content)
    href_news = selector.css("h3.tec--card__title a::attr(href)").getall()
    list_href_news = []
    for href in href_news:
        list_href_news.append(href)
    return list_href_news


# html = fetch("https://www.tecmundo.com.br/novidades")
# print(scrape_novidades(html))


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_url = selector.css("div.tec--list a.tec--btn::attr(href)").get()
    return next_page_url


# html = fetch("https://www.tecmundo.com.br/novidades")
# print(scrape_next_page_link(html))


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css("time::attr(datetime)").get()

    writer = (
        selector.css("a.tec--author__info__link::text").get()
        or selector.css(".tec--timestamp__item.z--font-bold a::text").get()
        or selector.css(".z--m-none.z--truncate.z--font-bold::text").get()
    )
    if writer:
        writer = writer.strip()

    shares_text = selector.css("div.tec--toolbar__item::text").get()
    shares_count = extract_number_from_string(shares_text)

    comments_text = selector.css("button#js-comments-btn::text").getall()[1]
    comments_count = extract_number_from_string(comments_text)

    summary_list = selector.xpath(
        '//div[has-class("tec--article__body")] //p[1]//text()'
    ).getall()
    summary = "".join(summary_list)

    sources = selector.css("div.z--mb-16 a.tec--badge::text").getall()
    formated_sources = remove_spaces(sources)

    categories = selector.css(
        "#js-categories a.tec--badge.tec--badge--primary::text"
    ).getall()
    formated_categories = remove_spaces(categories)

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": formated_sources,
        "categories": formated_categories,
    }


# https://careerkarma.com/blog/python-string-strip/
def remove_spaces(list):
    if list:
        list_with_spaces_removed = [i.strip() for i in list]
        return list_with_spaces_removed
    return list


# https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
def extract_number_from_string(string):
    if string:
        string_numbers = "".join(filter(lambda i: i.isdigit(), string))
        return int(string_numbers)
    return 0


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
