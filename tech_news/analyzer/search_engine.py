from tech_news.database import db
import re


def get_formated_news(query):
    news = db.news.find(query)
    return [(each_news["title"], each_news["url"]) for each_news in news]


# Requisito 6
def search_by_title(title):
    return get_formated_news({"title": re.compile(title, re.IGNORECASE)})


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
