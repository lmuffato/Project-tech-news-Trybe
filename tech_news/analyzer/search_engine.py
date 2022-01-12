from ..database import db


# Requisito 6
def search_by_title(title):
    found_news = db.news.find({"title": {"$regex": title, "$options": 'i'}})
    return [
        (news['title'], news['url'])
        for news in found_news
    ] or []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
