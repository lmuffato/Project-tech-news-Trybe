from datetime import datetime
import tech_news.database as db


def change_to_tuples(arr):
    to_return = []
    for i in arr:
        to_return.append((i["title"], i["url"]))
    return to_return


# Requisito 6
def search_by_title(title):
    news = db.search_news({
        "title": {
            "$regex": title,
            "$options": "i",
        },
    })
    to_return = change_to_tuples(news)
    
    return to_return


# Requisito 7
def search_by_date(date):
    try:
        """vlw maurício pela dica do strptime"""
        datetime.strptime(date, "%Y-%m-%d")
        news = db.search_news({
            "timestamp": {
                "$regex": date,
                "$options": "i",
            },
        })
        to_return = change_to_tuples(news)
        return to_return
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = db.search_news({
        "sources": {
            "$regex": source,
            "$options": "i",
        },
    })
    to_return = change_to_tuples(news)
    
    return to_return


# Requisito 9
def search_by_category(category):
    news = db.search_news({
        "categories": {
            "$regex": category,
            "$options": "i",
        },
    })
    to_return = change_to_tuples(news)
    
    return to_return
