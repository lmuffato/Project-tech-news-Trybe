from tech_news.database import search_news


def search_by_title(title):
    search_for_news = search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    list_news = []

    for result in search_for_news:
        news_result = (result["title"], result["url"])
        list_news.append(news_result)

    return list_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
