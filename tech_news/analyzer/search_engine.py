from tech_news.database import search_news
import time


# Requisito 6
def search_by_title(title):
    titulo = search_news({"title": {"$regex": title, "$options": "i"}})

    noticias = []
    for noticia in titulo:
        nova_noticia = (noticia["title"], noticia["url"])
        noticias.append(nova_noticia)
    return noticias


# Requisito 7
def search_by_date(date):
    try:
        time.strptime(date, "%Y-%m-%d")
        data = search_news({"timestamp": {"$regex": date}})
        noticias = []
        for noticia in data:
            nova_noticia = (noticia["title"], noticia["url"])
            noticias.append(nova_noticia)
        return noticias

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
