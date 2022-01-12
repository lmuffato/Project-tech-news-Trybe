import requests
import time
import parsel


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
        if item.css("link::attr(rel)").get() == "amphtml":
            url = item.css("link::attr(href)").get()
    return url


def get_shares_count(selector):
    shares_count = 0
    for word in selector.css("div.tec--toolbar__item::text").get().split():
        if word.isdigit():
            shares_count = int(word)
    return shares_count


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    url = get_url(selector)
    title = selector.css("h1#js-article-title::text").get()
    timestamp = selector.css("time#js-article-date::attr(datetime)").get()
    writer = selector.css("a.tec--author__info__link::text").get()
    shares_count = get_shares_count(selector)
    comments_count = selector.css(
        "button#js-comments-btn::attr(data-count)").get()
    item = selector.css("div.tec--article__body p").getall()
    item_list = parsel.Selector(item[0]).css("*::text").getall()
    summary = ""
    for text in item_list:
        summary += text
    tec_badges = selector.css("a.tec--badge::text").getall()
    categories = selector.css("a.tec--badge--primary::text").getall()
    sources = []
    for badge in tec_badges:
        if badge not in categories:
            sources.append(badge)
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


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
