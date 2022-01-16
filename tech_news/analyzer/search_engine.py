import re
from tech_news.database import search_news

# Visto o repositório do Alexandre Oliveira que esclareceu como
# realizar estas atividades


# Requisito 6
def search_by_title(title):
    titles = search_news({
        "title": re.compile(title, re.IGNORECASE)})
    if (len(titles)):
        return [(new["title"], new["url"]) for new in titles]
    else:
        return []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
