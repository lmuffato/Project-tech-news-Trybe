from ..database import search_news
from time import strptime


# Requisito 6
def search_by_title(title):
    list_news = search_news({"title": {"$regex": title, "$options": "i"}})
    data_news_list = []

    for list in list_news:
        data_news_list.append((list["title"], list["url"]))
    return data_news_list


# Requisito 7
def search_by_date(date):
    data_news_list = []
    try:
        strptime(date, "%Y-%m-%d")
        list_news_data = search_news(
            {"timestamp": {"$regex": date, "$options": "i"}}
        )
        for list in list_news_data:
            data_news_list.append((list["title"], list["url"]))
    except ValueError:
        raise ValueError("Data inválida")

    return data_news_list


# Requisito 8
def search_by_source(source):
    data_news_list = []
    list_news_data = search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )
    for list in list_news_data:
        data_news_list.append((list["title"], list["url"]))

    return data_news_list


# Requisito 9
def search_by_category(category):
    data_news_list = []
    list_news_data = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    for list in list_news_data:
        data_news_list.append((list["title"], list["url"]))

    return data_news_list
