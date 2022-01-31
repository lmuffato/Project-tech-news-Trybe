from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    find_news = search_news({"title": {"$regex": title, "$options": "i"}})
    list_news = []

    for new in find_news:
        result = (new["title"], new["url"])
        list_news.append(result)

    return list_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    list_news = []
    find_news = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    for new in find_news:
        list_news.append((new["title"], new["url"]))

    return list_news


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    find_news = search_news({"sources": {"$regex": source, "$options": "i"}})
    list_news = []

    for new in find_news:
        result = (new["title"], new["url"])
        list_news.append(result)

    return list_news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    find_news = search_news({"categories": {
        "$regex": category, "$options": "i"}})
    list_news = []

    for new in find_news:
        result = (new["title"], new["url"])
        list_news.append(result)

    return list_news
