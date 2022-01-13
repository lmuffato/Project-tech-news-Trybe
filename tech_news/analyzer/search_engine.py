import datetime
from tech_news.database import search_news


def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    if news_list:
        for news in news_list:
            result.append((news["title"], news["url"]))
    return result


# Requisito 7
# Validação do formato
# https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    news_list = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    result = []
    if news_list:
        for news in news_list:
            result.append((news["title"], news["url"]))
    return result
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    news_list = search_news({"sources": {"$regex": source, "$options": "i"}})
    result = []
    if news_list:
        for news in news_list:
            result.append((news["title"], news["url"]))
    return result
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    news_list = search_news(
        {"categories": {"$regex": category, "$options": "i"}})
    result = []
    if news_list:
        for news in news_list:
            result.append((news["title"], news["url"]))
    return result
    """Seu código deve vir aqui"""
