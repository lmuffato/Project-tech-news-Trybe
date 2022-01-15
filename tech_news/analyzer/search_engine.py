from ..database import search_news


# Requisito 6
def search_by_title(title):
    db_data = search_news({"title": {"$regex": title, "$options": "i"}})
    news_list = []

    for item in db_data:
        news = (item["title"], item["url"])
        news_list.append(news)

    return news_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    db_data = search_news({"sources": {"$regex": source, "$options": "i"}})
    news_list = []

    for item in db_data:
        news = (item["title"], item["url"])
        news_list.append(news)

    return news_list


# Requisito 9
def search_by_category(category):
    db_data = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    news_list = []

    for item in db_data:
        news = (item["title"], item["url"])
        news_list.append(news)

    return news_list
