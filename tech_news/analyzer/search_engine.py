from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news_by_title = search_news({'title': {'$regex': title, '$options': 'i'}})
    return [(n['title'], n['url']) for n in news_by_title]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
