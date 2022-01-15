from tech_news.database import db


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    # Ref. case insensitive:
    # https://stackoverflow.com/questions/8246019/case-insensitive-search-in-mongo

    query = {"title": {"$regex": title, "$options": "i"}}
    find_news = db.news.find(query)
    data = []

    for new in find_news:
        data.append((new["title"], new["url"]))

    return data


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
