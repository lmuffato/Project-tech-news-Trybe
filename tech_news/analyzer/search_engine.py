from tech_news.database import search_news
from datetime import datetime


def mapNews(new):
    newTuple = (new['title'], new['url'])
    print(newTuple)
    return newTuple


# Requisito 6
def search_by_title(title):
    queryDict = {'title': {'$regex': title, '$options': 'i'}}
    rawList = search_news(queryDict)
    test = list(map(mapNews, rawList))
    print(test)
    return test


# Requisito 7
def search_by_date(date):
    year, month, day = date.split('-')
    try:
        datetime(int(year), int(month), int(day))
        gte = datetime(int(year), int(month), (int(day) - 1)).isoformat()
        lte = datetime(int(year), int(month), (int(day) + 1)).isoformat()
        queryDict = {'timestamp': {'$gte': gte, '$lte': lte}}
        rawList = search_news(queryDict)
        return list(map(mapNews, rawList))
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
