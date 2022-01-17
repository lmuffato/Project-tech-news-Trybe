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

    selected_class = "link[rel=canonical]::attr(href)"
    url = selector.css(selected_class).get()

    selected_title = "h1::text"
    title = selector.css(selected_title).get()

    select_writer = ".z--font-bold ::text"
    writer = selector.css(select_writer).get().strip()

    selected_summary = "meta[name=description]::attr(content)"
    summary = selector.css(selected_summary).get()

    selected_sources = ".z--mb-16 .tec--badge::text"
    sources = selector.css(selected_sources).getall()
    list_sources = []
    for source in sources:
        new_sources = source.strip()
        list_sources.append(new_sources)

    print(list_sources)

    selected_categories = ".tec--badge--primary ::text"
    categories = selector.css(selected_categories).getall()
    new_list = []
    for category in categories:
        new_category = category.strip()
        new_list.append(new_category)

    selected_comments = "button::attr(data-count)"
    comments = selector.css(selected_comments).get()

    selected_shares = ".tec--toolbar__item::text"
    shares_count = selector.css(selected_shares).get()

    selected_timestamp = "time::attr(datetime)"
    timestamp = selector.css(selected_timestamp).get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": int(comments),
        "shares_count": int(shares_count.split()[0]) if shares_count else 0,
        "summary": summary,
        "sources": list_sources,
        "categories": new_list,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
