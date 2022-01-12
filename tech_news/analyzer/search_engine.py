# from pymongo import MongoClient
from tech_news.database import db, client


# Requisito 6
def search_by_title(title):
    title_list = []

    with client:
        for new in db.news.find({"title": title}):
            print(title)
            title_list.append((new["title"], new["url"]))

    print("Lista final", title_list)

    return title_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
