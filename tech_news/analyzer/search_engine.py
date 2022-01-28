import re
import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    table = search_news({"title": re.compile(title, re.IGNORECASE)})

    return [(row["title"], row["url"]) for row in table]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")

    table = search_news({"timestamp": re.compile(date)})

    return [(row["title"], row["url"]) for row in table]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    table = search_news({"sources": re.compile(source, re.IGNORECASE)})

    return [(row["title"], row["url"]) for row in table]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    table = search_news({"categories": re.compile(category, re.IGNORECASE)})

    return [(row["title"], row["url"]) for row in table]
