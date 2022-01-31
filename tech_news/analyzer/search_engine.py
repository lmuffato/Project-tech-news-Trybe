from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    filter_list = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(new["title"], new["url"]) for new in filter_list]


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    filters_list = search_news({"timestamp": {"$regex": date}})
    list = []
    for news in filters_list:
        list.append((news["title"], news["url"]))
    return list


# Requisito 8
def search_by_source(source):
    filters_list = search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )
    return [(new["title"], new["url"]) for new in filters_list]


# Requisito 9
def search_by_category(category):
    filters_list = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    return [(new["title"], new["url"]) for new in filters_list]
