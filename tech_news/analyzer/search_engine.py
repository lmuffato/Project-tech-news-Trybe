from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    # pesquisa sobre busca usando case sensitive
    # https://docs.mongodb.com/manual/reference/method/db.collection.find/
    # https://docs.mongodb.com/manual/reference/operator/query/regex/#mongodb-query-op.-regex

    results = search_news({"title": {"$regex": title, "$options": "i"}})
    response = []

    for result in results:
        title_search = result["title"]
        url_search = result["url"]

        response.append(title_search)
        response.append(url_search)

    if response:
        return [tuple(response)]
    else:
        return []


# Requisito 7
def search_by_date(date):
    try:
        # fonte:
        # https://stackoverflow.com/questions/47771911/python-regular-expression-date-yyyy-mm-dd-hhmmss
        valid_date = datetime.strptime(date, "%Y-%m-%d")

        if valid_date:
            formated_return = []
            results = search_news({"timestamp": {"$regex": date}})

            for result in results:
                formated_return.append(result["title"])
                formated_return.append(result["url"])

            if len(formated_return) > 0:
                return [tuple(formated_return)]
            else:
                return []

    except ValueError:
        return "Data inválida"


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
