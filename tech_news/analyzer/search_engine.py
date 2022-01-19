from tech_news.database import find_news
from datetime import datetime


def search_by_title(title):
    content = find_news()
    result = list()
    for new in content:
        if new["title"].upper() == title.upper():
            result.append(tuple([new["title"], new["url"]]))
    return result or list()


def search_by_date(date):
    date_formating = "%Y-%m-%d"
    try:
        datetime.strptime(date, date_formating)
        content = find_news()
        response = list()
        for new in content:
            if new["timestamp"][0:10] == date:
                response.append(tuple([new["title"], new["url"]]))
        return response or []
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    content = find_news()
    response = list()

    for new in content:
        sources = list()

        for source_item in new["sources"]:
            sources.append(source_item.upper())

        if source.upper() in sources:
            response.append(tuple([new["title"], new["url"]]))

    return response or []


def search_by_category(category):
    content = find_news()
    response = list()
    for new in content:
        categories = list()
        for categories_item in new["categories"]:
            categories.append(categories_item.upper())
        if category.upper() in categories:
            response.append(tuple([new["title"], new["url"]]))
    return response or []
