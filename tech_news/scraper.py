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
class Noticia:
    def __init__(self, html_content):
        self.html_content = html_content
        self.selector = Selector(text=self.html_content)

    def get_categories(self):
        categories_query = '.tec--badge--primary::text'

        categories = self.selector.css(categories_query).getall()
        return [cat.strip() for cat in categories]

    def get_sources(self):
        categories = self.get_categories()

        sources_and_categs_query = '.tec--badge::text'
        sources_and_categs = self.selector.css(
            sources_and_categs_query).getall()

        sources_and_categs = [sc.strip() for sc in sources_and_categs]

        return [tag for tag in sources_and_categs if tag not in categories]

    def get_summary(self):
        summary_query = '.tec--article__body p:first-child *::text'

        return ''.join(self.selector.css(summary_query).getall())

    def get_comments_count(self):
        comments_count_query = '#js-comments-btn::attr(data-count)'

        return int(self.selector.css(comments_count_query).get())

    def get_shares_count(self):
        shares_count_query = '.tec--toolbar__item::text'

        shares_string = self.selector.css(shares_count_query).get()
        shares_count = [
            int(c) for c in shares_string.split() if c.isdigit()
        ][0]

        return shares_count

    def get_writer(self):
        writer_query = '.tec--author__info__link::text'

        writer = self.selector.css(writer_query).get()
        print(writer)
        return writer.strip()

    def get_timestamp(self):
        timestamp_query = '#js-article-date::attr(datetime)'

        return self.selector.css(timestamp_query).get()

    def get_title(self):
        title_query = '.tec--article__header__title::text'

        return self.selector.css(title_query).get()

    def get_url(self):
        url_query = 'head link[rel=canonical]::attr(href)'

        return self.selector.css(url_query).get()


def scrape_noticia(html_content):
    noticia = Noticia(html_content)

    return {
        'url': noticia.get_url(),
        'title': noticia.get_title(),
        'timestamp': noticia.get_timestamp(),
        'writer': noticia.get_writer(),
        'shares_count': noticia.get_shares_count(),
        'comments_count': noticia.get_comments_count(),
        'summary': noticia.get_summary(),
        'sources': noticia.get_sources(),
        'categories': noticia.get_categories()
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
