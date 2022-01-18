from tech_news.database import db
from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news['title'], news['url']) for news in news]


# Requisito 7
def search_by_date(date):
    format = "%Y-%m-%d"
    try:
        date_obj = datetime.datetime.strptime(date, format)
        str_date = str(date_obj.date())
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news = db.news.find(
            {"timestamp": {"$regex": (str_date)}},
            {"title": 1, "url": 1, "_id": 0},
        )
        return [(new["title"], new["url"]) for new in news]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
