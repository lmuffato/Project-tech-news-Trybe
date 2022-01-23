from datetime import datetime
import re
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    return [
        (noticia["title"], noticia["url"])
        for noticia in search_news({"title": re.compile(title, re.IGNORECASE)})
    ]


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
    return [
        (noticia["title"], noticia["url"])
        for noticia in search_news(
            {"sources": re.compile(source, re.IGNORECASE)}
        )
    ]


# Requisito 9
def search_by_category(category):
    return [
        (noticia["title"], noticia["url"])
        for noticia in search_news(
            {"categories": re.compile(category, re.IGNORECASE)}
        )
    ]
