from tech_news.database import db
import re
from tech_news.database import search_news
import datetime


def get_formated_news(query):
    news = db.news.find(query)
    return [(each_news["title"], each_news["url"]) for each_news in news]


# Requisito 6
def search_by_title(title):
    return get_formated_news({"title": re.compile(title, re.IGNORECASE)})


def validate_date_regex(date):
    regex = re.search(r"(\d{4})-\d{2}-\d{2}", date)
    if regex is None or int(regex[1]) < 2000:
        raise ValueError("Data inválida")


# Requisito 7
def search_by_date(date):
    """Method to search news by date"""

    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    query = {"timestamp": {"$regex": date}}
    data_news = search_news(query)
    result = [(news["title"], news["url"]) for news in data_news]
    return result


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
