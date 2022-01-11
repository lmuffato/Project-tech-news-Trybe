import requests
import time
import re
from parsel import Selector


def selector_html(html_content):
    selector = Selector(text=html_content)

    return selector

# Requisito 1


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None

    if response.status_code != 200:
        return None
    else:
        return response.text


# Requisito 2


def scrape_novidades(html_content):
    html_text = selector_html(html_content)

    urls = html_text.css(
      "h3.tec--card__title a.tec--card__title__link::attr(href)"
      ).getall()

    return urls

# Requisito 2 foi entendindo utilizando o seguinte link:
# https://parsel.readthedocs.io/en/latest/usage.html#nesting-selectors

# Requisito 3


def scrape_next_page_link(html_content):
    html_text = selector_html(html_content)

    next_url = html_text.css(
      "a.tec--btn.tec--btn--lg.tec--btn-" +
      "-primary.z--mx-auto.z--mt-48::attr(href)"
      ).get()

    return next_url


# Requisito 4


def scrape_noticia(html_content):
    html_text = selector_html(html_content)

    noticia_title = html_text.css(
      "article.tec--article h1#js-article-title::text"
      ).get()

    noticia_time = html_text.css(
      "article.tec--article time#js-article-date::attr(datetime)"
      ).get()

    noticia_writer = html_text.css(
      "article.tec--article a.tec--author__info__link::text"
      ).get()

    noticia_shares_count = html_text.css(
      "article.tec--article div.tec--toolbar__item::text"
      ).get()

    shares_count = int(re.findall('[0-9]+', noticia_shares_count)[0])

    print({
      noticia_title,
      noticia_time,
      noticia_writer,
      shares_count
      })


# Requisito 5


def get_tech_news(amount):
    """Seu código deve vir aqui"""
