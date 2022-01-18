from ..database import search_news


# Requisito 6
def search_by_title(title):
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []

    for item in data:
        titles = (item["title"], item["url"])
        result.append(titles)

    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
