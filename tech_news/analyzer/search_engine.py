from tech_news.database import search_news
import re
import time


# Requisito 6
def search_by_title(title):
    if title == "":
        return []
    news_list = []
    response = search_news({"title": title.capitalize()})
    if len(response) == 0:
        return response
    for item in response:
        news_typle = item["title"], item["url"]
        news_list.append(news_typle)
    return news_list


# Requisito 7
def search_by_date(date):
    try:
        time.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    news_list = []
    regex = re.compile(date)
    response = search_news({"timestamp": regex})
    if len(response) == 0:
        return response
    for item in response:
        news_typle = item["title"], item["url"]
        news_list.append(news_typle)
    return news_list


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
