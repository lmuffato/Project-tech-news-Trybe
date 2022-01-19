from tech_news.database import search_news

from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(query)
    data = []

    for news in news:
        data.append((news["title"], news["url"]))

    return data


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        query = {"timestamp": {"$regex": date}}
        data = search_news(query)

        if data:
            for news in data:
                return [(news["title"], news["url"])]
        return []

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
