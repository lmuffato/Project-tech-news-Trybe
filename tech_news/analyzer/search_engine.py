import re
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news_by_title = search_news({
        "title": re.compile(title, re.IGNORECASE)})
    if (len(news_by_title)):
        return [(item["title"], item["url"]) for item in news_by_title]
    else:
        return []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
