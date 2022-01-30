from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        result = requests.get(url, timeout=3)
        time.sleep(1)
        if (result.status_code == 200):
            return result.text
        raise(ValueError)
    except (requests.Timeout, ValueError):
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    ref = '.tec--list__item article h3 a.tec--card__title__link::attr(href)'
    news = selector.css(ref).getall()
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    ref = '.tec--list a.tec--btn::attr(href)'
    next_page_link = selector.css(ref).get()
    return next_page_link


# Requisito 4
def get_url(selector):
    url = None
    head_links = selector.css('head link').getall()
    for link in head_links:
        rel_selector = Selector(text=link)
        rel_value = rel_selector.css('link::attr(rel)').get()
        if (rel_value == 'canonical'):
            url = rel_selector.css('link::attr(href)').get()
    return url


def get_title(selector):
    title_id = '#js-article-title::text'
    title = selector.css(f'{title_id}').get()
    return title


def get_time(selector):
    time_id = '#js-article-date::attr(datetime)'
    timestamp = selector.css(f'{time_id}').get()
    return timestamp


def get_writer(selector):
    author_link = 'a.tec--author__info__link::text'
    author_p = '.z--font-bold ::text'
    # https://github.com/tryber/sd-010-a-tech-news/pull/64/files
    author = (
        selector.css(f'{author_link}').get()
        or selector.css(f'{author_p}').get()
        )
    return author.strip() if author else None


def get_shares_count(selector):
    author_div = '.tec--author'
    shares = '.tec--toolbar__item::text'
    shares_count = selector.css(f'{author_div} {shares}').re_first('\d')

    if shares_count is None:
        shares_count = 0
    else:
        shares_count = int(shares_count)

    return shares_count


def get_comments_count(selector):
    container = '.tec--author'
    comments = '.tec--toolbar__item'
    btn = '.tec--btn::text'
    count = selector.css(f'{container} {comments} {btn}').re_first('\d')

    if count is None:
        count = 0
    else:
        count = int(count)

    return count


def get_summary(selector):
    body = '.tec--article__body'
    summary_array = selector.css(f'{body} > p:first-child *::text').getall()
    summary = ''.join(summary_array)
    return summary


def get_sources(selector):
    container = '.z--mb-16'
    sources_class = '.tec--badge'
    sources_array = selector.css(f'{container} {sources_class}::text').getall()
    sources = []
    for source in sources_array:
        sources.append(source.strip())
    return sources


def get_categories(selector):
    container = '#js-categories'
    categories_class = '.tec--badge'
    array = selector.css(f'{container} {categories_class}::text').getall()
    categories = []
    for category in array:
        categories.append(category.strip())
    return categories


def scrape_noticia(html_content):
    new_information = {}
    selector = Selector(text=html_content)

    new_information['url'] = get_url(selector)
    new_information['title'] = get_title(selector)
    new_information['timestamp'] = get_time(selector)
    new_information['writer'] = get_writer(selector)
    new_information['shares_count'] = get_shares_count(selector)
    new_information['comments_count'] = get_comments_count(selector)
    new_information['summary'] = get_summary(selector)
    new_information['sources'] = get_sources(selector)
    new_information['categories'] = get_categories(selector)

    return new_information


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
