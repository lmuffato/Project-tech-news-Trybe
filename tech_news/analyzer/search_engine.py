from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    # Ref. case insensitive:
    # https://stackoverflow.com/questions/8246019/case-insensitive-search-in-mongo

    query = {"title": {"$regex": title, "$options": "i"}}
    find_news = search_news(query)
    data = []

    for new in find_news:
        data.append((new["title"], new["url"]))

    return data


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        query = {"timestamp": {"$regex": date, "$options": "i"}}
        find_news = search_news(query)
        data = []

        for new in find_news:
            data.append((new["title"], new["url"]))

        return data
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
