import re
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news = []
    for noticia in search_news({"title": re.compile(title, re.IGNORECASE)}):
        news.append((noticia["title"], noticia["url"]))
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
