import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    data = Selector(text=html_content)
    links = data.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    data = Selector(text=html_content)
    btn_mostrar_mais = data.css("div.tec--list a.tec--btn::attr(href)").get()
    if btn_mostrar_mais:
        return btn_mostrar_mais
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    data = Selector(text=html_content)
    news_url = data.css("meta[property='og:url']::attr(content)").get()
    news_title = data.css("h1.tec--article__header__title::text").get()
    news_timestamp = data.css(
        "div.tec--timestamp__item time::attr(datetime)"
    ).get()
    news_writer = (
        data.css(".tec--author__info__link::text").get()
        or data.css("div.tec--timestamp__item a::text").get()
        or data.css("div.tec--author__info p.z--font-bold::text").get()
    )
    news_shares_count = data.css("tec--toolbar__item::text").get()
    news_comments_count = data.css("#js-comments-btn::attr(data-count)").get()
    news_summary = "".join(
        data.css(".tec--article__body > p:first-child *::text").getall()
    )
    news_sources = [
        item.strip() for item in data.css("div.z--mb-16 div a::text").getall()
    ]
    news_categories = [
        item.strip() for item in data.css("#js-categories a::text").getall()
    ]
    news_data = {
        "url": news_url,
        "title": news_title,
        "timestamp": news_timestamp,
        "writer": news_writer.strip() if news_writer else None,
        "shares_count": int(news_shares_count.split()[0])
        if news_shares_count
        else 0,
        "comments_count": int(news_comments_count)
        if news_comments_count
        else 0,
        "summary": news_summary,
        "sources": news_sources,
        "categories": news_categories,
    }
    return news_data


# Requisito 5
def get_tech_news(amount):
    url_base = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(url_base)
    news_links = scrape_novidades(html_content)
    links_cortados = []
    news_list = []

    while len(news_links) < amount:
        next_page_link = scrape_next_page_link(html_content)
        next_news = fetch(next_page_link)
        news_links.append(scrape_novidades(next_news))
    for link in news_links:
        html_content = fetch(link)
        news_list.append(scrape_noticia(html_content))

    if len(news_list) > amount:
        for news in news_list[:amount]:
            links_cortados.append(news)
            create_news(news)
        return {amount: links_cortados}
    else:
        create_news(news_list)
        return {len(news_links): news_list}


print(get_tech_news(5))

# test = fetch("https://www.tecmundo.com.br/novidades")
# print(scrape_novidades(test))
# print(len(scrape_novidades(test)))

# print("Next page btn")
# print(scrape_next_page_link(test))

# print("Scrap Noticia")
# print(scrape_noticia(test))
