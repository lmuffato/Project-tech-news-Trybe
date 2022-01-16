from ..database import search_news
from datetime import datetime


# Requisito 6
# https://stackoverflow.com/questions/8246019/case-insensitive-search-in-mongo
def search_by_title(title):
    data_base_news = search_news({"title": {"$regex": title, "$options": "i"}})
    news = []

    for new in data_base_news:
        news_result = (new["title"], new["url"])
        news.append(news_result)

    return news


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
    """Seu código deve vir aqui"""
