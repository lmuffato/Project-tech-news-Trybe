from ..database import search_news
from time import strptime


def search_by_general(str_colum, str_criteria):
    data_news_list = []
    list_news_data = search_news(
        {str_colum: {"$regex": str_criteria, "$options": "i"}}
    )
    for list in list_news_data:
        data_news_list.append((list["title"], list["url"]))

    return data_news_list


# Requisito 6
def search_by_title(title):
    return search_by_general("title", title)


# Requisito 7
def search_by_date(date):
    try:
        strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    return search_by_general("timestamp", date)


# Requisito 8
def search_by_source(source):
    return search_by_general("sources", source)


# Requisito 9
def search_by_category(category):
    return search_by_general("categories", category)
