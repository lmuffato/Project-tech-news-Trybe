from tech_news.database import search_news
import time


# Requisito 6
def search_by_title(title):
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    news_list = []
    for news in search:
        selected_news = (news["title"], news["url"])
        news_list.append(selected_news)

    return news_list


# Requisito 7
def search_by_date(date):
    try:
        time.strptime(date, "%Y-%m-%d")
        search = search_news({"timestamp": {"$regex": date}})
        news_list = []
        for news in search:
            selected_news = (news["title"], news["url"])
            news_list.append(selected_news)

        return news_list

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
