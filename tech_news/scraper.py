import requests
import time

from requests.exceptions import URLRequired
import parsel

# URL = "https://www.tecmundo.com.br/novidades"


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)

        if response.status_code != 200:
            return None
        else:
            return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# print(fetch(URL))


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    lists = []

    lists = selector.css("h3.tec--card__title a::attr(href)").getall()

    # for item in selector.css(".tec--list__item"):
    #     url = item.css(".tec--card__title__link ::attr(href)").get()
    #     lists.append(url)

    return lists


# html = fetch(URL)
# print(scrape_novidades(html))


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    url = selector.css("a.tec--btn--lg ::attr(href)").get()

    return url


# html = fetch(URL)
# print(scrape_next_page_link(html))


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
