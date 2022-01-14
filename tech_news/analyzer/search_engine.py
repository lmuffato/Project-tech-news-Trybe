from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    list_mongo = find_news()
    find_title = [t for t in list_mongo if t["title"].lower() == title.lower()]
    list_duple = []
    for noticie in find_title:
        list_duple.append((noticie["title"], noticie["url"]))
    print(list_duple)
    return list_duple


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
