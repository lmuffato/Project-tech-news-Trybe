# from pymongo import MongoClient
from tech_news.database import db, client
import re
import datetime


# Requisito 6
def search_by_title(title):
    title_list = []

    with client:
        for new in db.news.find({"title": re.compile(title, re.IGNORECASE)}):

            title_list.append((new["title"], new["url"]))

    return title_list

# Conseguir deixar ele como case insensitive com o link:
# https://stackoverflow.com/questions/6266555/querying-mongodb-via-pymongo-in-case-insensitive-efficiently


# Requisito 7
def search_by_date(date):
    news_list = []

    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        with client:
            for new in db.news.find({"timestamp": {"$regex": date}}):
                news_list.append((new["title"], new["url"]))

    except ValueError:
        raise ValueError("Data inválida")

    return news_list

# Cheguei a utilizar a lib datetime por causa desse forum:
# https://stackoverflow.com/questions/9978534/match-dates-using-python-regular-expressions/9978701


# Requisito 8
def search_by_source(source):
    new_list = []

    with client:
        for new in db.news.find({
          "sources": re.compile(source, re.IGNORECASE)
          }):

            new_list.append((new["title"], new["url"]))

    return new_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
