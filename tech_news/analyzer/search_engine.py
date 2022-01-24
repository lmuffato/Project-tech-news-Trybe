from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": title, "$options": "i"}}
    results = search_news(query)
    return [(result["title"], result["url"]) for result in results]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        """Source:
        https://qastack.com.br/programming/
        16870663/how-do-i-validate-a-date-string-format-in-python"""
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    query = {"timestamp": {"$regex": date}}

    results = search_news(query)
    return [(result["title"], result["url"]) for result in results]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    query = {"sources": {"$regex": source, "$options": "i"}}
    results = search_news(query)
    return [(result["title"], result["url"]) for result in results]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    query = {"categories": {"$regex": category, "$options": "i"}}
    results = search_news(query)
    return [(result["title"], result["url"]) for result in results]
