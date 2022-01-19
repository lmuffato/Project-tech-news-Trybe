from tech_news.database import search_news

from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(query)
    data = []

    for news in news:
        data.append((news["title"], news["url"]))

    return data


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        query = {"timestamp": {"$regex": date}}
        data = search_news(query)

        if data:
            for news in data:
                return [(news["title"], news["url"])]
        return []

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": source, "$options": "i"}}
    data = search_news(query)
    news_list = []

    for news in data:
        news_found = (news["title"], news["url"])
        news_list.append(news_found)
    return news_list


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$regex": category, "$options": "i"}}
    data = search_news(query)

    result = []
    for news in data:
        found = (news["title"], news["url"])
        result.append(found)

    return result

