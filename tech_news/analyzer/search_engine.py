from tech_news.database import search_news
import time


# Requisito 6
def search_by_title(title):
    find_title = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    for news in find_title:
        note = (news["title"], news["url"])
        result.append(note)
    return result


# Requisito 7
def search_by_date(date):
    try:
        time.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    find_date = search_news({"timestamp": {"$regex": date}})
    result = []
    for news in find_date:
        note = (news["title"], news["url"])
        result.append(note)
    return result


# Requisito 8
def search_by_source(source):
    find_source = search_news(
        {"sources": {"$regex": source, "$options": "i"}})
    result = []
    for news in find_source:
        note = (news["title"], news["url"])
        result.append(note)
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
