from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": {'$regex': title, '$options': 'i'}})
    tuple_list = []
    for news in news_list:
        tuple_list.append((news["title"], news["url"]))
    return tuple_list


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    news_list = search_news({"timestamp": {"$regex": date}})
    tuple_list = []
    for news in news_list:
        tuple_list.append((news["title"], news["url"]))
    return tuple_list


# Requisito 8
def search_by_source(source):
    news_list = search_news({"sources": {'$regex': source, '$options': 'i'}})
    tuple_list = []
    for news in news_list:
        tuple_list.append((news["title"], news["url"]))
    return tuple_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
