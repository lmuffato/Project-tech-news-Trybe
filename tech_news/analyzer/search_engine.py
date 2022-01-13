from tech_news.database import db


# Requisito 6
def search_by_title(title):
    query = {"title": {'$regex': title, '$options': 'i'}}
    options = {"title": 1, "url": 1, "_id": 0}
    news_dict = list(db.news.find(query, options))
    tuplas_news = []

    for n in news_dict:
        tuplas_news.append((n["title"], n["url"]))

    return tuplas_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
