from datetime import datetime
from ..database import search_news


# Requisito 6
def search_by_title(title):
    data = search_news({"title": {"$regex": title, "$options": 'i'}})
    list = []
    for t in data:
        tupla = (t['title'], t['url'])
        list.append(tupla)
    return list


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    data = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    list = []
    for dates in data:
        tupla = (dates['title'], dates['url'])
        list.append(tupla)
    return list


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
