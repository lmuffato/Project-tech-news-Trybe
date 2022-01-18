import requests
import time
from parsel import Selector


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
    news_url = data.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).get()
    news_title = data.css(
        "h3.tec--card__title a.tec--card__title__link::text"
    ).get()
    news_timestamp = data.css("div.tec--timestamp__item::text").get()
    news_data = {
        "url": news_url,
        "title": news_title,
        "timestamp": news_timestamp,
    }
    print(news_data)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


test = fetch("https://www.tecmundo.com.br/novidades")
print(scrape_novidades(test))
print(len(scrape_novidades(test)))

print("Next page btn")
print(scrape_next_page_link(test))

print("Scrap Noticia")
print(scrape_noticia(test))
