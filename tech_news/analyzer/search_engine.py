import re
from tech_news.database import db


# source :
# https://stackoverflow.com/questions/6266555/querying-mongodb-via-pymongo-in-case-insensitive-efficiently
# Requisito 6
def search_by_title(title):
    news = list(db.news.find({"title": re.compile(title, re.IGNORECASE)}))
    titles_and_urls = [(new["title"], new["url"]) for new in news]
    return titles_and_urls


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
