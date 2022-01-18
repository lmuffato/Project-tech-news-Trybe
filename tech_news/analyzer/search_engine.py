from tech_news.database import search_news


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


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
