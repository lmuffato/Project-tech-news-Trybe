import requests
import time
from parsel import Selector
from tech_news.database import create_news
from tech_news.news_constructor import NewsConstructor


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links_list = []
    for news_link in selector.css("h3.tec--card__title"):
        link = news_link.css("a.tec--card__title__link::attr(href)").get()
        links_list.append(link)
    return links_list


# Documentação Parsel:
# https://parsel.readthedocs.io/en/latest/usage.html


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css("a.tec--btn::attr(href)").get()
    if next_page_link:
        return next_page_link
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news_dict = {
        "url": "",
        "title": "",
        "timestamp": "",
        "writer": "",
        "shares_count": 0,
        "comments_count": 0,
        "summary": "",
        "sources": [],
        "categories": []
    }
    for news in selector.xpath('//html[contains(@lang, "pt-BR")]'):
        news_url = NewsConstructor.extract_news_url(news)
        title = NewsConstructor.extract_news_title(news)
        writer = NewsConstructor.get_news_author(news)
        summary = NewsConstructor.get_news_summary(news)
        categories_list = NewsConstructor.get_news_categories(news)
        sources_list = NewsConstructor.get_news_sources(news)
        comments_count = NewsConstructor.get_comments_count(news)
        shares_count = NewsConstructor.get_shares_count(news)
        timestamp = NewsConstructor.get_datetime(news)

        news_dict["url"] = news_url
        news_dict["title"] = title
        news_dict["writer"] = writer
        news_dict["summary"] = summary
        news_dict["categories"] = categories_list
        news_dict["sources"] = sources_list
        news_dict["shares_count"] = shares_count
        news_dict["comments_count"] = comments_count
        news_dict["timestamp"] = timestamp

    return news_dict


# Source:
# Sobre strip():
# https://dev.to/jacob777baltimore/python-remove-all-whitespace-4m3n


def get_more_news(news_list, amount, html_content):
    if news_list and amount and html_content:
        while len(news_list) < amount:
            link_to_next_page = scrape_next_page_link(html_content)
            next_page = fetch(link_to_next_page)
            news_urls = scrape_novidades(next_page)
            news_list.extend(news_urls)
    return news_list


def iterate_news_list(news_list, amount):
    result_list = []
    for news in news_list[:amount]:
        page = fetch(news)
        result_list.append(scrape_noticia(page))
    return result_list


# Requisito 5
def get_tech_news(amount):
    try:
        news_list = []
        html = fetch("https://www.tecmundo.com.br/novidades")

        news_list.extend(scrape_novidades(html))
        result = []
        if len(news_list) < amount:
            news_updated_list = get_more_news(news_list, amount, html)
            result = iterate_news_list(news_updated_list, amount)
            create_news(result)
        else:
            result = iterate_news_list(news_list, amount)
            create_news(result)
        return result
    except ValueError:
        return ""
