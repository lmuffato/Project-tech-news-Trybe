from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None

    except requests.ReadTimeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls = selector.css(
        ".tec--list__item .tec--card__thumb__link::attr(href)"
    ).getall()
    if not urls:
        return []
    else:
        return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    selected_class = ".tec--list .tec--btn::attr(href)"
    next_page_link = selector.css(selected_class).get()
    if not next_page_link:
        return None
    else:
        return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    def scrape_strip(list_item):
        new_list = []
        for item in list_item:
            new_item = item.strip()
            new_list.append(new_item)

        return new_list

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1::text").get()
    writer = selector.css(".z--font-bold ::text").get().strip()
    summary = selector.css("meta[name=description]::attr(content)").get()
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    """ list_sources = []
    for source in sources:
        new_sources = source.strip()
        list_sources.append(new_sources)

    print(list_sources)"""

    categories = selector.css(".tec--badge--primary ::text").getall()
    """ new_list = []
    for category in categories:
        new_category = category.strip()
        new_list.append(new_category)"""

    comments = selector.css("button::attr(data-count)").get()
    shares_count = selector.css(".tec--toolbar__item::text").get()
    timestamp = selector.css("time::attr(datetime)").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": int(comments),
        "shares_count": int(shares_count.split()[0]) if shares_count else 0,
        "summary": summary,
        "sources": scrape_strip(sources),
        "categories": scrape_strip(categories),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
