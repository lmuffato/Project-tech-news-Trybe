from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    find_news = search_news({"title": {"$regex": title, "$options": "i"}})
    list_news = []

    for news in find_news:
        result = (news["title"], news["url"])
        list_news.append(result)

    return list_news


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    find_news = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    list_news = []

    for news in find_news:
        result = (news["title"], news["url"])
        list_news.append(result)

    return list_news


# Requisito 8
def search_by_source(source):
    find_news = search_news({"sources": {"$regex": source, "$options": "i"}})
    list_news = []

    for news in find_news:
        result = (news["title"], news["url"])
        list_news.append(result)

    return list_news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
