from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": f"{title}", "$options": "-i"}}

    arrNews = search_news(query)
    if arrNews:
        return [(new["title"], new["url"]) for new in arrNews]
    else:
        return []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        # https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    query = {"timestamp": {"$regex": f"{date}"}}
    arrNews = search_news(query)
    if arrNews:
        return [(new["title"], new["url"]) for new in arrNews]
    else:
        return []


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
