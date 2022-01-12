from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    queryDict = {'title': {'$regex': title, '$options': 'i'}}
    rawList = search_news(queryDict)

    def mapNews(new):
        newTuple = (new['title'], new['url'])
        print(newTuple)
        return newTuple
    test = list(map(mapNews, rawList))
    print(test)
    return test


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
