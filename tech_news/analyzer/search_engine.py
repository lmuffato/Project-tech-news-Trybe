from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": {'$regex': title, '$options': 'i'}})
    tuple_list = []
    for news in news_list:
        tuple_list.append((news["title"], news["url"]))
    return tuple_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
