from ..database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    db_data = search_news({"title": {"$regex": title, "$options": "i"}})
    news_list = []

    for item in db_data:
        news = (item["title"], item["url"])
        news_list.append(news)

    return news_list


# Requisito 7
def search_by_date(date):

    try:
        format = "%Y-%m-%d"
        datetime.datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Data inválida")

    db_data = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    news_list = []

    for item in db_data:
        news = (item["title"], item["url"])
        news_list.append(news)

    return news_list


# Fonte req 7:
# https://www.kite.com/python/answers/how-to-validate-a-date-string-format-in-python

# Requisito 8
def search_by_source(source):
    db_data = search_news({"sources": {"$regex": source, "$options": "i"}})
    news_list = []

    for item in db_data:
        news = (item["title"], item["url"])
        news_list.append(news)

    return news_list


# Requisito 9
def search_by_category(category):
    db_data = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    news_list = []

    for item in db_data:
        news = (item["title"], item["url"])
        news_list.append(news)

    return news_list
