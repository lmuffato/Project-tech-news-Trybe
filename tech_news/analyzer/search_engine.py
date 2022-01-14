from tech_news.database import find_news
import datetime


# Requisito 6
def search_by_title(title):
    list_mongo = find_news()
    find_title = [t for t in list_mongo if t["title"].lower() == title.lower()]
    list_duple = []
    for noticie in find_title:
        list_duple.append((noticie["title"], noticie["url"]))

    return list_duple


# Requisito 7
def extend_search_by_date(date):
    list_mongo = find_news()
    find_data = []
    for obj in list_mongo:
        format_date = obj["timestamp"]
        format_date = format_date.split("T")
        if format_date[0] == date:
            find_data.append(obj)

    list_duple = []
    for noticie in find_data:
        list_duple.append((noticie["title"], noticie["url"]))
    return list_duple


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        return extend_search_by_date(date)


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
