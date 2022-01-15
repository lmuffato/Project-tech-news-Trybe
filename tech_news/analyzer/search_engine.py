from tech_news.database import search_news


# Requisito 6


def search_by_title(title):
    """Seu código deve vir aqui"""
    result = []
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    for notice in data:
        titles = (notice["title"], notice["url"])
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
