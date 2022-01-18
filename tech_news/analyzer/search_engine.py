from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = []
    db_news = search_news({"title": {"$regex": title, "$options": "i"}})
    for notice in db_news:
        news.append((notice["title"], notice["url"]))
    return news

# https://docs.mongodb.com/manual/reference/operator/query/regex/


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
