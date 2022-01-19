import re
import datetime
from tech_news.database import search_news


def results_to_tuple_array(result):
    return [(element["title"], element["url"]) for element in result]


# Requisito 6
def search_by_title(title):
    search_result = search_news({"title": re.compile(title, re.IGNORECASE)})
    formated_result = results_to_tuple_array(search_result)
    return formated_result


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    search_result = search_news({"timestamp": {"$regex": date}})
    formated_result = results_to_tuple_array(search_result)
    return formated_result


# Requisito 8
def search_by_source(source):
    search_result = search_news({"sources": re.compile(source, re.IGNORECASE)})
    formated_result = results_to_tuple_array(search_result)
    return formated_result


# Requisito 9
def search_by_category(category):
    search_result = search_news(
        {"categories": re.compile(category, re.IGNORECASE)}
    )
    formated_result = results_to_tuple_array(search_result)
    return formated_result
