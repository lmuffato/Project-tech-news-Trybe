from tech_news.database import search_news


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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
