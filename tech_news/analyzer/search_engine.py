from tech_news.database import search_news
from tech_news.database import db


# Requisito 6
def search_by_title(title):
    query = {"title": {'$regex': title, '$options': 'i'}}
    options = {"title": 1, "url": 1, "_id": 0}
    news_list = db.news.find(query, options)
    data = [(doc["title"], doc["url"]) for doc in news_list]
    return data


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
