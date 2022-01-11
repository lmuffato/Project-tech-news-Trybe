import requests
import time
from parsel import Selector
URL_BASE = "https://www.tecmundo.com.br/novidades"


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        else:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    content = selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()

    return [item for item in content]


# x = scrape_novidades(fetch(URL_BASE))
# print(x)