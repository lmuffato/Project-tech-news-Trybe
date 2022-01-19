from tech_news.database import search_news
from datetime import datetime


# Run avaliator Run
def search_by_title(title):
    result = search_news({"title": {"$regex": title, "$options": "i"}})
    if result:
        for item in result:
            return [(item["title"], item["url"])]
    return []


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        result = search_news({"timestamp": {"$regex": date}})
        if result:
            for item in result:
                return [(item["title"], item["url"])]
        return []
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    result = search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )
    if result:
        for item in result:
            return [(item["title"], item["url"])]
    return []


def search_by_category(category):
    result = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    if result:
        for item in result:
            return [(item["title"], item["url"])]
    return []
