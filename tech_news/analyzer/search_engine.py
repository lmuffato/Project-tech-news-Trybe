from tech_news.database import search_news
import re


# Requisito 6
def search_by_title(title):
    news = search_news({"title": re.compile(title, re.IGNORECASE)})
    return [(item["title"], item["url"]) for item in news]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    news = search_news({"sources": re.compile(source, re.IGNORECASE)})
    return [(item["title"], item["url"]) for item in news]


# Requisito 9
def search_by_category(category):
    news = search_news({"categories": re.compile(category, re.IGNORECASE)})
    return [(item["title"], item["url"]) for item in news]
