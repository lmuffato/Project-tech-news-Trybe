# Requisito 6
from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    """Seu código deve vir aqui"""
    title_news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(new["title"], new["url"]) for new in title_news]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        data = search_news({"timestamp": {"$regex": date}})
        if data:
            for i in data:
                return [(i["title"], i["url"])]
        return []
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
