from ..database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    news = []

    for item in data:
        noticia = (item["title"], item["url"])
        news.append(noticia)

    return news


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")

    data = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    news = []

    for item in data:
        noticia = (item["title"], item["url"])
        news.append(noticia)

    return news


# Requisito 8
def search_by_source(source):
    data = search_news({"sources": {"$regex": source, "$options": "i"}})
    news = []

    for item in data:
        noticia = (item["title"], item["url"])
        news.append(noticia)

    return news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
