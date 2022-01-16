from ..database import search_news


# Requisito 6
def search_by_title(title):
    all_news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news['title'], news['url']) for news in all_news]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
