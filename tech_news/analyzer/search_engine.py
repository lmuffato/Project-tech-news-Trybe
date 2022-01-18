import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    db_news = search_news({"title": {"$regex": title, "$options": "i"}})
    list_of_news = []

    for news in db_news:
        news_to_be_added = (news["title"], news["url"])
        list_of_news.append(news_to_be_added)

    return list_of_news


# Requisito 7
def search_by_date(date):
    # https://www.kite.com/python/answers/how-to-validate-a-date-string-format-in-python
    format = "%Y-%m-%d"

    try:
        datetime.datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Data inválida")

    db_news = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    list_of_news = []

    for news in db_news:
        news_to_be_added = (news["title"], news["url"])
        list_of_news.append(news_to_be_added)

    return list_of_news


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
