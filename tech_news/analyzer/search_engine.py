import re
from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = [
        (noticia["title"], noticia["url"])
        for noticia in search_news({"title": re.compile(title, re.IGNORECASE)})
    ]
    return news


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        response = search_news({"timestamp": re.compile(date)})
        news = [
            (noticia["title"], noticia["url"])
            for noticia in response
            if response
        ]
        return news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = [
        (noticia["title"], noticia["url"])
        for noticia in search_news(
            {"sources": re.compile(source, re.IGNORECASE)}
        )
    ]
    return news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
