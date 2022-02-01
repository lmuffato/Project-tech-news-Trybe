import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1


def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    query = 'h3.tec--card__title a.tec--card__title__link::attr(href)'
    return selector.css(query).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link = selector.css('a.tec--btn::attr(href)').getall()
    if link:
        return link[0]
    else:
        return None


# Feito com ajuda
# Requisito 4
def scrape_noticia(html_content):
    news = {}
    selector = Selector(text=html_content)
    url = selector.css('head link[rel=canonical]::attr(href)').get()
    title = selector.css('h1.tec--article__header__title::text').get()
    timestamp = selector.css('time::attr(datetime)').get()
    writer = selector.css('.z--font-bold *::text').get()
    sc = selector.css('div.tec--toolbar__item::text').re_first(r'\d+')
    comments_count = selector.css('#js-comments-btn::attr(data-count)').get()
    summary_query = 'div.tec--article__body > p:first-child *::text'
    summary_tag = selector.css(summary_query).getall()
    summary = ''.join(summary_tag)
    sources = selector.css('div.z--mb-16 a::text').getall()
    sources = [s.strip() for s in sources]
    categories = selector.css('div#js-categories a.tec--badge::text').getall()
    categories = [c.strip() for c in categories]
    news['url'] = url
    news['title'] = title
    news['timestamp'] = timestamp
    news['writer'] = writer.strip() if writer else None
    news['shares_count'] = int(sc) if sc else 0
    news['comments_count'] = int(comments_count)
    news['summary'] = summary
    news['sources'] = sources
    news['categories'] = categories
    return news


# Requisito 5
def get_tech_news(amount):
    url = 'https://www.tecmundo.com.br/novidades'

    html = fetch(url)
    links = scrape_novidades(html)
    while len(links) < amount:
        next_link = scrape_next_page_link(html)
        html = fetch(next_link)
        links.extend(scrape_novidades(html))

    news = []
    for link in links[:amount]:
        html = fetch(link)
        scraped = scrape_noticia(html)
        news.append(scraped)

    create_news(news)
    return news
