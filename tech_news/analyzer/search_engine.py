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
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
