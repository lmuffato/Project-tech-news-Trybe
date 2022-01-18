from tech_news.database import search_news
import datetime


# https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362
# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    find_bd_news = search_news({"title": {"$regex": title,
                                          "$options": 'i'}})

    new_tupla = []
    for new in find_bd_news:
        new_tupla.append((new["title"], new["url"]))
    return new_tupla


# https://qastack.com.br/programming/16870663/how-do-i-validate-a-date-string-format-in-python
# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    find_bd_news = search_news({"timestamp": {"$regex": date}})

    new_tupla = []
    for new in find_bd_news:
        if new is not []:
            new_tupla.append((new["title"], new["url"]))
        else:
            return []

    return new_tupla



# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
