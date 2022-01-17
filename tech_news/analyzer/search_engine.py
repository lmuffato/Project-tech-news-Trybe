from tech_news.database import search_news
import re


# Requisito 6
def search_by_title(title):
    news = search_news({"title": re.compile(title, re.IGNORECASE)})
    return [(new["title"], new["url"]) for new in news]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
