from tech_news.database import search_news
import time


# Requisito 6
def search_by_title(title):
    title = search_news({"title": {"$regex": title, "$options": "i"}})
    info_list = []
    for news in title:
        selected_news = (news["title"], news["url"])
        info_list.append(selected_news)

    return info_list


# Requisito 7
def search_by_date(date):
    try:
        time.strptime(date, "%Y-%m-%d")
        date = search_news({"timestamp": {"$regex": date}})
        info_list = []
        for news in date:
            selected_news = (news["title"], news["url"])
            info_list.append(selected_news)

        return info_list

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    source = search_news({"sources": {"$regex": source, "$options": "i"}})

    info_list = []
    for news in source:
        selected_news = (news["title"], news["url"])
        info_list.append(selected_news)

    return info_list


# Requisito 9
def search_by_category(category):
    category = search_news(
        {"categories": {"$regex": category, "$options": "i"}})

    info_list = []
    for news in category:
        selected_news = (news["title"], news["url"])
        info_list.append(selected_news)

    return info_list
