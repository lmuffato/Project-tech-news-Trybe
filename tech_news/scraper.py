from typing import Union
from requests.models import Response

import requests
import time
from functools import reduce
from parsel import Selector


# Requisito 1
def fetch(url: str) -> Union[Response, None]:
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if(response.status_code != 200):
            return None
        return response.text
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content: str) -> list:
    selector = Selector(text=html_content)
    # É preciso resgatar os links via <h3>
    # ao invés de direto pelo <a> para retornar quantidade correta
    news_links = [a.attrib['href'] for a in selector.css(
        'h3.tec--card__title').css('a')]
    return news_links


# Requisito 3
def scrape_next_page_link(html_content: str) -> list:
    selector = Selector(text=html_content)
    next_page_link_href = selector.css('a.tec--btn::attr(href)').get()
    return next_page_link_href


# Requisito 4
def scrape_noticia(html_content: str):
    selector = Selector(text=html_content)
    meta_with_url = [e for e in selector.css('meta') if 'property' in e.attrib
                     and e.attrib['property'] == 'og:url']
    url = meta_with_url[0].attrib['content']
    title = selector.css('h1.tec--article__header__title::text').get()
    timestamp = selector.css('#js-article-date').attrib['datetime']
    writer = selector.css(
        '.z--font-bold ::text').get()
    toolbar_items = selector.css('div.tec--toolbar__item::text').getall()
    shares_count = (reduce(lambda a, b: a + b, filter(
        str.isdigit, toolbar_items[0]))) if len(toolbar_items) > 0 else 0
    comment_btn_chld = selector.css('#js-comments-btn::text').getall()
    comments_count = reduce(lambda a, b: a + b, filter(
        str.isdigit, next(e for e in comment_btn_chld if not str.isspace(e))))
    """ https://stackoverflow.com/questions/58904013/
    extract-text-content-from-nested-html-while-
    excluding-some-specific-tags-scrapy """
    summary = ''.join(
        Selector(text=selector.css(
            'div.tec--article__body p').getall()[0]).css('*::text').extract())
    sources_and_categories = selector.css('a.tec--badge')
    sources = [link.css('*::text').extract()[0].strip()
               for link in sources_and_categories
               if 'tec--badge--primary' not in link.attrib['class']]
    categories = [link.css('*::text').extract()[0].strip()
                  for link in sources_and_categories
                  if 'tec--badge--primary' in link.attrib['class']]
    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer.strip() if writer is not None else writer,
        'shares_count': int(shares_count),
        'comments_count': int(comments_count),
        'summary': summary,
        'sources': sources,
        'categories': categories
        }


print(scrape_noticia(fetch('https://www.tecmundo.com.br/minha-serie/215168-10-viloes-animes-extremamente-inteligentes.htm')))


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
