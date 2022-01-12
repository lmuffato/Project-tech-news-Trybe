from tech_news.database import search_news


# Requisito 6
def search_by_title(title):

    query = {"title": {"$regex": title, "$options": 'i'}}
    # Case-insensitive(option i): https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362#create+a+case-insensitive+%24regex+query+in+pymongo+using+%24options
    search_result = search_news(query)
    result = [(news["title"], news["url"]) for news in search_result]
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
