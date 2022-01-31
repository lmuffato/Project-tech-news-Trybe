import re
from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = []
    for noticia in search_news({"title": re.compile(title, re.IGNORECASE)}):
        news.append((noticia["title"], noticia["url"]))
    return news


# Requisito 7
def search_by_date(date):
    try:
        news = []
        datetime.strptime(date, "%Y-%m-%d")
        response_search = search_news({"timestamp": re.compile(date)})
        if response_search:
            for noticia in response_search:
                news.append((noticia["title"], noticia["url"]))
        return news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = []
    for noticia in search_news({"sources": re.compile(source, re.IGNORECASE)}):
        news.append((noticia["title"], noticia["url"]))
    return news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
