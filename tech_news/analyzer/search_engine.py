import re
from tech_news.database import db
from datetime import datetime


# source :
# https://stackoverflow.com/questions/6266555/querying-mongodb-via-pymongo-in-case-insensitive-efficiently
# Requisito 6
def search_by_title(title):
    news = list(db.news.find({"title": re.compile(title, re.IGNORECASE)}))
    titles_and_urls = [(new["title"], new["url"]) for new in news]
    return titles_and_urls


# source:
# https://stackoverflow.com/questions/4709652/python-regex-to-match-dates
# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        news = list(db.news.find({"timestamp": {"$regex": date}}))
        titles_and_urls = [(new["title"], new["url"]) for new in news]
        return titles_and_urls
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = list(db.news.find({"sources": {"$regex": source, "$options": "i"}}))
    titles_and_urls = [(new["title"], new["url"]) for new in news]
    return titles_and_urls


# Requisito 9
def search_by_category(category):
    news = list(
        db.news.find({"categories": {"$regex": category, "$options": "i"}})
    )
    titles_and_urls = [(new["title"], new["url"]) for new in news]
    return titles_and_urls
