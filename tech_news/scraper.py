import requests
import time
import parsel
# Requisito 1


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    links = selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
        ).getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    next_page_link = selector.css("a.tec--btn::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)

    writer_selector = selector.css(".z--font-bold ::text").get()
    writer = writer_selector.strip() if writer_selector else None

    shares = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    shares_count = int(shares) if shares else 0

    comments = selector.css("#js-comments-btn::text").re_first(r"\d+")
    comments_count = int(comments) if comments else 0

    summary_selector = selector.css(
      ".tec--article__body > p:first_child *::text").getall()
    summary = "".join(summary_selector).strip()

    sources_selector = selector.css("div.z--mb-16 a::text").getall()
    sources = [source.strip() for source in sources_selector]

    categories_selector = selector.css("#js-categories a::text").getall()
    categories = [category.strip() for category in categories_selector]

    response = {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("#js-article-title ::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories

    }
    return response


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
