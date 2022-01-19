from tech_news.database import search_news


def search_by_title(title):
    titleNews = search_news({"title": {"$regex": title, "$options": "i"}})
    newsList = []

    for news in titleNews:
        newNews = (news["title"], news["url"])
        newsList.append(newNews)
    return newsList


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
