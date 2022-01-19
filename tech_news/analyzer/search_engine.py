import time
from tech_news.database import search_news


def search_by_title(title):
    titleNews = search_news({"title": {"$regex": title, "$options": "i"}})
    newsList = []
    for news in titleNews:
        newNews = (news["title"], news["url"])
        newsList.append(newNews)
    return newsList


def search_by_date(date):
    try:
        time.strptime(date, "%Y-%m-%d")
        searchTiem = search_news({"timestamp": {"$regex": date}})
        newsList = []
        for news in searchTiem:
            newsT = (news["title"], news["url"])
            newsList.append(newsT)
        return newsList
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    searchSource = search_news({
        "sources": {"$regex": source, "$options": "i"}})
    newsList = []
    for news in searchSource:
        newsT = (news["title"], news["url"])
        newsList.append(newsT)
    return newsList


def search_by_category(category):
    searchCategory = search_news({
        "categories": {"$regex": category, "$options": "i"}})
    newsList = []
    for news in searchCategory:
        newsT = (news["title"], news["url"])
        newsList.append(newsT)
    return newsList
