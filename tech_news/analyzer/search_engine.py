from ..database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    news = []

    for item in data:
        noticia = (item["title"], item["url"])
        news.append(noticia)

    return news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
