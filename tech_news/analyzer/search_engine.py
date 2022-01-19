from tech_news.database import search_news
from datetime import datetime
import re


# https://blog.geekhunter.com.br/python-regex/
# https://docs.python.org/3/library/re.html

# Requisito 6
def search_by_title(title):
    news = search_news({"title": re.compile(title, re.IGNORECASE)})
    return [(item["title"], item["url"]) for item in news]


# Requisito 7
def search_by_date(date):
    # https://www.programiz.com/python-programming/datetime/strptime
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    news = search_news({"timestamp": {"$regex": date}})
    return [(item["title"], item["url"]) for item in news]


# Requisito 8
def search_by_source(source):
    news = search_news({"sources": re.compile(source, re.IGNORECASE)})
    return [(item["title"], item["url"]) for item in news]


# Requisito 9
def search_by_category(category):
    news = search_news({"categories": re.compile(category, re.IGNORECASE)})
    return [(item["title"], item["url"]) for item in news]
