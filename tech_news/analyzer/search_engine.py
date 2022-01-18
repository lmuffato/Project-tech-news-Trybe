from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    data_base = search_news({"title": {"$regex": title, "$options": "i"}})
    noticias = []

    for noticia in data_base:
        news = (noticia["title"], noticia["url"])
        noticias.append(news)
    return noticias


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    noticia = []
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    data_base = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    for data in data_base:
        new = (data["title"], data["url"])
        noticia.append(new)
    return noticia


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    noticia = []
    data_base = search_news({"sources": {"$regex": source, "$options": "i"}})
    for data in data_base:
        source = (data["title"], data["url"])
        noticia.append(source)
    return noticia


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
