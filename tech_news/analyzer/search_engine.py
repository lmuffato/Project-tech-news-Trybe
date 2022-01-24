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


def mount_tupla(list):
    list_to_mount = []

    if len(list) == 0:
        return []

    for result in list:
        list_to_mount.append(result["title"])
        list_to_mount.append(result["url"])

    return [tuple(list_to_mount)]


# Requisito 7
def search_by_date(date):
    try:
        # fonte:
        # https://stackoverflow.com/questions/47771911/python-regular-expression-date-yyyy-mm-dd-hhmmss
        valid_date = datetime.strptime(date, "%Y-%m-%d")

        if valid_date:
            results = search_news({"timestamp": {"$regex": date}})
            result = mount_tupla(results)
            return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    results = search_news({"writer": {"$regex": source, "$options": "i"}})
    print("RESULTSSSSS", results)
    result = mount_tupla(results)
    return result


# Requisito 9
def search_by_category(category):
    results = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    result = mount_tupla(results)
    return result
