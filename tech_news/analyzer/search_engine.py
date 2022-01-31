from ..database import search_news
from datetime import datetime

# Requisito 6
def search_by_title(title):
    results = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(item['title'], item['url']) for item in results]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
