from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    search_for_news = search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    list_news = []

    for result in search_for_news:
        news_result = (result["title"], result["url"])
        list_news.append(news_result)

    return list_news


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    result = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    return [(news["title"], news["url"]) for news in result]


def search_by_source(source):
    result = search_news({"sources": {"$regex": source, "$options": "i"}})
    return [(news["title"], news["url"]) for news in result]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
