from datetime import datetime
from re import IGNORECASE, compile

from tech_news.database import search_news

# https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = search_news({"title": compile(title, IGNORECASE)})
    results = list()
    for new in news:
        results.append((new["title"], new["url"]))
    return results


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    news = search_news({"timestamp": compile(date)})
    result = list()
    for new in news:
        result.append((new["title"], new["url"]))
    return result


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news = search_news({"sources": compile(source, IGNORECASE)})
    result = list()
    for new in news:
        result.append((new["title"], new["url"]))
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    news = search_news({"categories": compile(category, IGNORECASE)})
    result = list()
    for new in news:
        result.append((new["title"], new["url"]))
    return result
