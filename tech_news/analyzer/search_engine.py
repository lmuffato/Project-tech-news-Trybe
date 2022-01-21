from ..database import search_news
import time


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    db_data = search_news({"title": {"$regex": title, "$options": "i"}})
    news_list = []

    for item in db_data:
        news = (item["title"], item["url"])
        news_list.append(news)

    return news_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    # https://stackoverflow.com/questions/16527878/check-if-line-is-a-timestamp-in-python
    try:
        time.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    data = search_news({"timestamp": {"$regex": date}})
    news_list = []
    for item in data:
        news = (item["title"], item["url"])
        news_list.append(news)
    return


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    db_data = search_news({"sources": {"$regex": source, "$options": "i"}})
    news_list = []

    for item in db_data:
        news = (item["title"], item["url"])
        news_list.append(news)

    return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    data = search_news({"categories": {"$regex": category, "$options": "i"}})
    news_list = []

    for item in data:
        news = (item["title"], item["url"])
        news_list.append(news)

    return news_list
