from tech_news.database import search_news
from datetime import datetime


# source: https://github.com/tryber/sd-010-a-tech-news/pull/25/files
# Requisito 6
def search_by_title(title):
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []

    for item in data:
        titles = (item["title"], item["url"])
        result.append(titles)

    return result


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    data = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    new_list = []

    for item in data:
        news = (item["title"], item["url"])
        new_list.append(news)
    return new_list


# Requisito 8
def search_by_source(source):
    data = search_news({"sources": {"$regex": source, "$options": "i"}})
    news_list = []

    for item in data:
        news = (item["title"], item["url"])
        news_list.append(news)
    return news_list


# Requisito 9
def search_by_category(category):
    data = search_news({"categories": {"$regex": category, "$options": "i"}})
    news_list = []

    for item in data:
        news = (item["title"], item["url"])
        news_list.append(news)

    return news_list
