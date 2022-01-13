from tech_news.database import search_news
from datetime import datetime


def formated_search(query):
    search_result = search_news(query)
    result = [(news["title"], news["url"]) for news in search_result]
    return result


# Requisito 6
def search_by_title(title):

    query = {"title": {"$regex": title, "$options": 'i'}}
    # Case-insensitive(option i):
    # https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362#create+a+case-insensitive+%24regex+query+in+pymongo+using+%24options
    result = formated_search(query)
    return result


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        # datetime strptime:
        # https://www.programiz.com/python-programming/datetime/strptime
        query = {"timestamp": {
            '$regex': date
        }}
        result = formated_search(query)
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": source, "$options": 'i'}}
    result = formated_search(query)
    return result


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$regex": category, "$options": 'i'}}
    result = formated_search(query)
    return result
