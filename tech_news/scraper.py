import requests
from time import sleep
import parsel
from tech_news.database import create_news


# Requisito 1
def fetch(url, delay=1, timeout=3):
    try:
        sleep(delay)
        response = requests.get(url, timeout=timeout)
    except (requests.ReadTimeout, requests.HTTPError):
        return None
    else:
        if response.status_code == 200:
            return response.text


# Requisito 2
def scrape_novidades(html_content):
    links = []
    response = parsel.Selector(html_content)
    for link in response.css("h3.tec--card__title"):
        result = link.css("a.tec--card__title__link::attr(href)").get()
        links.append(result)
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    response = parsel.Selector(html_content)
    try:
        next_page = response.css("a.tec--btn--lg::attr(href)").get()
        return next_page
    except TimeoutError:
        return None


# Requisito 4
# requisito feito observando o do repositorio do Eduardo Seije
def scrape_noticia(html_content):
    selector = parsel.Selector(text=html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    author = selector.css(".z--font-bold *::text").get()
    writer = author.strip() if author else None
    shares_count = selector.css(".tec--toolbar__item::text").get()
    news_shares_count = (
        shares_count.strip().split(" ")[0] if shares_count else 0
    )
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    comments_count = comments_count if comments_count else 0
    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    summary = "".join(summary)

    sources = []
    for source in selector.css(".z--mb-16 div a::text").getall():
        sources.append(source.strip())

    categories = []
    for category in selector.css("#js-categories a::text").getall():
        categories.append(category.strip())

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(news_shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
# requisito feito observando o do repositorio do Iago Ferreira
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    result = fetch(url)
    news = scrape_novidades(result)
    news_array = []
    while len(news) < amount:
        next_page_link = scrape_next_page_link(result)
        result = fetch(next_page_link)
        new_to_array = scrape_novidades(result)
        news += new_to_array
    for adress in news[:amount]:
        the_new = fetch(adress)
        news_array.append(scrape_noticia(the_new))
    create_news(news_array)
    return news_array
