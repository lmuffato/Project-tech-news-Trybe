from parsel import Selector
import requests
import time
import re


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if(response.status_code == 200):
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls = selector.css('.tec--card__info h3 a::attr(href)').getall()
    if(urls):
        return urls
    return []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    btn_next_page = selector.css('.tec--btn--primary::attr(href)').get()
    if(btn_next_page):
        return btn_next_page
    return None


def get_url(selector):
    return selector.css('link[rel=canonical]::attr(href)').get()


def get_title(selector):
    return selector.css('.tec--article__header__title::text').get()


def get_timestamp(selector):
    return selector.css('.tec--timestamp__item time::attr(datetime)').get()


def get_writer(selector):
    writer = selector.css(
        '.tec--author__info__link::text,'
        '.tec--timestamp--lg .z--font-bold a::text,'
        '.tec--author__info p::text').get()
    if(not writer):
        return None
    return writer.strip()


def get_shares_count(selector):
    shares_count_string = selector.css(
        '.tec--toolbar .tec--toolbar__item::text').get()
    if(not shares_count_string):
        return 0
    # Source https://pythonguides.com/python-find-number-in-string/
    return int(re.findall('[0-9]+', shares_count_string)[0])


def get_comments_count(selector):
    return int(selector.css('#js-comments-btn::attr(data-count)').get())


def get_summary(selector):
    summary_list = selector.css(
        '.tec--article__body p:nth-child(1) *::text').getall()
    return ''.join(summary_list)


def stripe_list(list):
    new_list = []
    for element in list:
        if(element):
            new_list.append(element.strip())
    return new_list


def get_sources(selector):
    sources_list = (selector.css(
        '.tec--article__body-grid .z--mb-16 .tec--badge::text'
        ).getall())
    return stripe_list(sources_list)


def get_categories(selector):
    categories_list = selector.css(
        '.tec--article__body-grid .tec--badge--primary::text').getall()
    return stripe_list(categories_list)


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = get_url(selector)
    title = get_title(selector)
    timestamp = get_timestamp(selector)
    writer = get_writer(selector)
    shares_count = get_shares_count(selector)
    comments_count = get_comments_count(selector)
    summary = get_summary(selector)
    sources = get_sources(selector)
    categories = get_categories(selector)
    page_dict = {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'shares_count': shares_count,
        'comments_count': comments_count,
        'summary': summary,
        'sources': sources,
        'categories': categories
        }

    return page_dict


# Requisito 5
def get_tech_news(amount):
    pass
    """Seu código deve vir aqui"""
