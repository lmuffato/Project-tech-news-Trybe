import requests
import time
import parsel

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    list = []
    for item in selector.css("div.tec--list__item"):
        link = item.css("a.tec--card__title__link::attr(href)").get()
        list.append(link)
    return list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    next_page_link = selector.css("a.tec--btn::attr(href)").get()
    if next_page_link:
        return next_page_link
    else:
        return None


def get_url(selector):
    url = ""
    for item in selector.css("link"):
        if item.css("link::attr(rel)").get() == "canonical":
            url = item.css("link::attr(href)").get()
    return url.strip()


def get_author(selector):
    writer_raw_a = selector.css("a.tec--author__info__link::text").get()
    writer_raw_div = selector.css("p.z--m-none::text").get()
    writer_raw_link = None
    for item in selector.css("a"):
        if "autor" in item.css("a::attr(href)").get():
            writer_raw_link = item.css("a::text").get()
    if writer_raw_a:
        writer = writer_raw_a.strip()
    if writer_raw_link:
        writer = writer_raw_link.strip()
    else:
        writer = writer_raw_div.strip()
    return writer


def get_shares_count(selector):
    shares_count = 0
    phrase = selector.css("div.tec--toolbar__item::text").get()
    if phrase:
        for word in phrase.split():
            if word.isdigit():
                shares_count = int(word)
    return shares_count


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    url = get_url(selector)
    title = selector.css("h1#js-article-title::text").get()
    timestamp = selector.css("time#js-article-date::attr(datetime)").get()
    writer = get_author(selector)
    shares_count = get_shares_count(selector)
    comments_count = int(selector.css(
        "button#js-comments-btn::attr(data-count)").get())
    item = selector.css("div.tec--article__body p").getall()
    item_list = parsel.Selector(item[0]).css("*::text").getall()
    summary = ""
    for text in item_list:
        summary += text
    tec_badges = selector.css("a.tec--badge::text").getall()
    categories_raw = selector.css("a.tec--badge--primary::text").getall()
    categories = []
    for item in categories_raw:
        categories.append(item.strip())
    sources = []
    for badge in tec_badges:
        if badge not in categories_raw:
            sources.append(badge.strip())
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


def limit_list(list, amount):
    final_news_url_list = []
    for url in list:
        if len(final_news_url_list) < amount:
            final_news_url_list.append(url)
    return final_news_url_list


# Requisito 5
def get_tech_news(amount):
    news_url_list = []
    html_pg_1 = fetch("https://www.tecmundo.com.br/novidades")
    html_pg_atual = html_pg_1
    url_list = scrape_novidades(html_pg_atual)
    url_next_pg = scrape_next_page_link(html_pg_atual)
    while len(news_url_list) < amount:
        for url in url_list:
            news_url_list.append(url)
        html_pg_atual = fetch(url_next_pg)
    final_news_url_list = limit_list(news_url_list, amount)
    news_list = []
    for news_url in final_news_url_list:
        news_html = fetch(news_url)
        news = scrape_noticia(news_html)
        news_list.append(news)
    create_news(news_list)
    return news_list
