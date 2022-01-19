import time
import requests
from tech_news.database import create_news
from parsel import Selector


def fetch(url):
    try:
        content = requests.get(url, timeout=3)
        time.sleep(1)
        if content.status_code == 200:
            return content.text
        return None
    except requests.ReadTimeout:
        return None


def scrape_novidades(html_content):
    selector = Selector(html_content)
    i = selector.css("h3 > a[class='tec--card__title__link']::attr(href)")
    return i.getall()


def scrape_next_page_link(html_content):
    selector = Selector(html_content).css(".tec--btn::attr(href)").get()
    return selector


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    news = dict()
    news["url"] = selector.css("link[rel=canonical]::attr(href)").get()

    news["title"] = selector.css("#js-article-title::text").get()

    news["timestamp"] = selector.css("#js-article-date::attr(datetime)").get()

    news["writer"] = selector.css(
        '.z--font-bold *::text'
        ).get().strip() if True else None

    get_share = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    news["shares_count"] = int(get_share) if get_share else 0

    get_comments = selector.css("#js-comments-btn::text").re_first(r"\d+")
    news["comments_count"] = int(get_comments) if get_comments else 0

    news["summary"] = "".join(selector.css(
        ".tec--article__body > p:first-of-type *::text"
    ).getall()).strip()

    get_source = selector.css(".z--mb-16 div a::text").getall()
    news["sources"] = [source.strip() for source in get_source]

    get_category = selector.css("#js-categories a::text").getall()
    news["categories"] = [category.strip() for category in get_category]

    return news


def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    titles = list()
    news = list()
    while len(news) < amount:
        news = news + scrape_novidades(fetch(url))
        url = scrape_next_page_link(fetch(url))
    for content in news[:amount]:
        content_link = fetch(content)
        titles.append(scrape_noticia(content_link))
    create_news(titles)
    return titles
