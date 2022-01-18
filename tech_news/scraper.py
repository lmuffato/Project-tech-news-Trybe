import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    news_urls = []
    selector = Selector(text=html_content)
    css_query = 'main .tec--card__title__link::attr(href)'
    news_urls = selector.css(css_query).getall()

    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    query = '.tec--btn::attr(href)'

    next_button_url = selector.css(query).get()
    if next_button_url == '':
        return None
    return next_button_url


# Requisito 4
def get_categories_noticia(html_content):
    selector = Selector(text=html_content)

    categories_query = '.tec--badge--primary::text'

    return selector.css(categories_query).getall()


def get_sources_noticia(html_content):
    selector = Selector(text=html_content)

    categories = get_categories_noticia(html_content)

    sources_and_categs_query = '.tec--badge::text'
    sources_and_categories = selector.css(sources_and_categs_query).getall()

    return [item for item in sources_and_categories if item not in categories]


def get_summary_noticia(html_content):
    selector = Selector(text=html_content)

    summary_query = '.tec--article__body p:first-child *::text'

    return ''.join(selector.css(summary_query).getall())


def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url_query = 'head link[rel=canonical]::attr(href)'
    title_query = '.tec--article__header__title::text'
    timestamp_query = '#js-article-date::attr(datetime)'
    writer_query = '.tec--author__info__link::text'
    shares_count_query = '.tec--toolbar__item::text'
    comments_count_query = '#js-comments-btn::attr(data-count)'

    return {
        'url': selector.css(url_query).get(),
        'title': selector.css(title_query).get(),
        'timestamp': selector.css(timestamp_query).get(),
        'writer': selector.css(writer_query).get(),
        'shares_count': selector.css(shares_count_query).get(),
        'comments_count': selector.css(comments_count_query).get(),
        'summary': get_summary_noticia(html_content),
        'sources': get_sources_noticia(html_content),
        'categories': get_categories_noticia(html_content)
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
