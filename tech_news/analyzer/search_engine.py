from tech_news.database import db


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    title = title.title()
    results = db.news.find({"title": title})
    return [(result["title"], result["url"]) for result in results]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
