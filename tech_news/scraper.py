from requests import get, Timeout
from parsel import Selector
from tech_news.database import create_news
import time


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = get(url, timeout=3)
    except Timeout:
        return None
    if response.status_code == 200:
        return response.text
    else:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    dicti = {}
    dicti['url'] = selector.css('link[rel=canonical]::attr(href)').get()
    dicti['title'] = selector.css('#js-article-title::text').get()
    dicti['timestamp'] = selector.css('#js-article-date::attr(datetime)').get()
    writer = selector.css('.z--font-bold *::text').get()
    if writer:
        dicti['writer'] = str(writer).strip()
    else:
        dicti['writer'] = None
    shares = selector.css('.tec--toolbar__item::text').get()
    if not shares:
        shares_count = 0
    else:
        shares_count = str(shares).split()[0]
    dicti['shares_count'] = int(shares_count)
    comments_count = selector.css('#js-comments-btn::attr(data-count)').get()
    dicti['comments_count'] = int(comments_count)
    dicti['summary'] = ''.join(selector.css(
        '.tec--article__body > p:nth-child(1) ::text').getall())
    sources = selector.css('.z--mb-16 .tec--badge::text').getall()
    dicti['sources'] = [str(source).strip() for source in sources]
    categories = selector.css('#js-categories a::text').getall()
    dicti['categories'] = [str(category).strip() for category in categories]

    return dicti


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    the_urls = selector.css(
        '.tec--list h3 .tec--card__title__link::attr(href)').getall()
    if not the_urls:
        return []
    else:
        return the_urls


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    the_url = selector.css(".tec--list a.tec--btn::attr(href)").get()
    if not the_url:
        return None
    else:
        return the_url


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    news_list = []
    url = 'https://www.tecmundo.com.br/novidades'

    while len(news_list) < amount:
        all_links = scrape_novidades(fetch(url))
        for link in all_links:
            scraped_info = scrape_noticia(fetch(link))
            if len(news_list) < amount:
                news_list.append(scraped_info)
        url = scrape_next_page_link(fetch(url))
    create_news(news_list)
    return news_list
