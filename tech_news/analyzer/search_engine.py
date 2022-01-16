from ..database import search_news


# Requisito 6
def search_by_title(title):
    list_news = search_news({"title": {"$regex": title, "$options": "i"}})
    data_news_list = []

    for list in list_news:
        data_news_list.append((list["title"], list["url"]))
    return data_news_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
