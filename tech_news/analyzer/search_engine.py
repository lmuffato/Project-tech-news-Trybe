from ..database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    data = search_news({"title": {"$regex": title, "$options": 'i'}})
    list = []
    for t in data:
        tupla = (t['title'], t['url'])
        list.append(tupla)
    return list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
