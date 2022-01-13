import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
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
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    card_title_link = ".tec--card__info h3 a::attr(href)"
    news_links = selector.css(card_title_link).getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_button_link = "a.tec--btn--lg::attr(href)"
    next_page_url = selector.css(next_button_link).get()
    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    # Ref. para alguns endereços CSS: Jodiel Briesemeister
    # Repositório: https://github.com/tryber/sd-010-a-tech-news/pull/5/files
    selector = Selector(text=html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article h1::text").get()
    time_stamp = ".tec--article time::attr(datetime)"
    timestamp = selector.css(time_stamp).get()
    writer = selector.css(".z--font-bold *::text").get()

    if writer:
        writer = writer.strip()
    else:
        writer = None

    shares_count = selector.css("div.tec--toolbar__item::text").get()

    if shares_count:
        shares_count = int(shares_count.split()[0])
    else:
        shares_count = 0

    comments_address = "button.tec--btn ::attr(data-count)"
    comments_counter = int(selector.css(comments_address).get())

    summary_address = "div.tec--article__body > p:first-child *::text"
    summary = selector.css(summary_address).getall()
    complete_summary = "".join(summary).strip()

    sources_list = selector.css(".z--mb-16 .tec--badge::text").getall()
    sources = []
    for source in sources_list:
        sources.append(source.strip())

    categories_list = selector.css("a.tec--badge--primary ::text").getall()
    categories = []
    for categorie in categories_list:
        categories.append(categorie.strip())

    formated_data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_counter,
        "summary": complete_summary,
        "sources": sources,
        "categories": categories,
    }

    return formated_data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    # Bug do summary do req. 04 que quebra o req. 05
    # resolvido com ajuda de Gabriel Pereira, T10-A.
    news_url = "https://www.tecmundo.com.br/novidades"
    news_links = []
    news_data = []

    while len(news_links) < amount:
        news_html = fetch(news_url)
        news_links.extend(scrape_novidades(news_html))
        news_url = scrape_next_page_link(news_html)

    for new_url in news_links[:amount]:
        news_html = fetch(new_url)
        news = scrape_noticia(news_html)
        news_data.append(news)

    create_news(news_data)
    return news_data
