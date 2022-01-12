import requests
import time
import re
import math
from parsel import Selector

import tech_news.database as database


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

    noticia_url = html_text.css(
      "head meta[property='og:url']::attr(content)"
      ).get()

    noticia_title = html_text.css(
      "article.tec--article h1#js-article-title::text"
      ).get()

    noticia_time = html_text.css(
      "article.tec--article time#js-article-date::attr(datetime)"
      ).get()

    noticia_writer = html_text.css(
      ".z--font-bold ::text"
      ).get()

    if not noticia_writer:
        writer = None
    else:
        writer = noticia_writer.strip()

    noticia_shares_count = html_text.css(
      "article.tec--article div.tec--toolbar__item::text"
      ).get()

    if not noticia_shares_count:
        shares_count = 0
    else:
        shares_count = int(re.findall('[0-9]+', noticia_shares_count)[0])

    noticia_summary = html_text.css(
      "article.tec--article div.tec--article__body p:first_child *::text"
      ).getall()

    summary = "".join(noticia_summary).strip()

    noticia_sources = html_text.css(
      "article.tec--article div.z--mb-16 a.tec--badge::text"
      ).getall()

    sources = [source.strip() for source in noticia_sources]

    noticia_categories = html_text.css(
      "article.tec--article div#js-categories a.tec--badge::text"
      ).getall()

    categories = [category.strip() for category in noticia_categories]

    noticia_organized = dict({
        "url": noticia_url,
        "title": noticia_title,
        "timestamp": noticia_time,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": 0,
        "summary": summary,
        "sources": sources,
        "categories": categories
    })

    return noticia_organized

# Utilização do Regex através do link:
# https://pythonguides.com/python-find-number-in-string/

# Utilização do *::text com o getall() e transformação em string:
# https://parsel.readthedocs.io/en/latest/usage.html
# https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python

# Como obter a url foi feita olhando a documentação:
# https://parsel.readthedocs.io/en/latest/usage.html

# Requisito 5


def get_tech_news(amount):
    news_by_amount = []
    # count_news = 1

    news_page_fetch = fetch("https://www.tecmundo.com.br/novidades/")
    news_catched = scrape_novidades(news_page_fetch)

    # print('Print dos catcheds', news_catched)
    print('Primeiro len', len(news_catched))

    if amount > 20:
        count_pages = 1
        number_of_pages = math.ceil(amount / 20)
        print('Numero de Pages', number_of_pages)

        while count_pages < number_of_pages:
            another_page_link = scrape_next_page_link(news_page_fetch)
            html_for_another_page = fetch(another_page_link)

            news_page_fetch = html_for_another_page

            news_for_another_page = scrape_novidades(html_for_another_page)

            for link in news_for_another_page:
                news_catched.append(link)
                # print('Novo len', len(news_catched))

            count_pages += 1

            # print(news_catched)

    print('Len final', len(news_catched))

    for new in news_catched[:amount]:
        # print('Test do new', new)
        new_html = fetch(new)
        new_scraped = scrape_noticia(new_html)

        news_by_amount.append(new_scraped)

    database.create_news(news_by_amount)

    return news_by_amount

    # print('Result', news_by_amount)
