import re
from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news_by_title = search_news({
        "title": re.compile(title, re.IGNORECASE)})
    if (len(news_by_title)):
        return [(new["title"], new["url"]) for new in news_by_title]
    else:
        return []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    news_by_date = search_news({"timestamp": {"$regex": date}})
    if (len(news_by_date)):
        return [(new["title"], new["url"]) for new in news_by_date]
    else:
        return []


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
