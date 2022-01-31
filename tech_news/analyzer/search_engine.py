from ..database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    results = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(item['title'], item['url']) for item in results]


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")

    result = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    return [(news['title'], news['url']) for news in result]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
