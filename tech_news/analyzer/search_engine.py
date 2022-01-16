from ..database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    all_news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news['title'], news['url']) for news in all_news]


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")

    all_news = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    return [(news['title'], news['url']) for news in all_news]


# Requisito 8
def search_by_source(source):
    all_news = search_news({"sources": {"$regex": source, "$options": "i"}})
    return [(news['title'], news['url']) for news in all_news]


# Requisito 9
def search_by_category(category):
    all_news = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
        )
    return [(news['title'], news['url']) for news in all_news]
