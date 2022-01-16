from ..database import search_news


# Requisito 6
# https://stackoverflow.com/questions/8246019/case-insensitive-search-in-mongo
def search_by_title(title):
    data_base_news = search_news({"title": {"$regex": title, "$options": "i"}})
    news = []

    for new in data_base_news:
        news_result = (new["title"], new["url"])
        news.append(news_result)

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
