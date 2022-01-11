import re
from tech_news.database import search_news
import datetime


def search6789(property, string):
    news_obj = search_news({property: re.compile(string, flags=re.I)})
    news_tuple_list = [(new["title"], new["url"]) for new in news_obj]
    return news_tuple_list


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    return search6789("title", title)


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        # criatividade: nomearam o módulo e a classe como datetime
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return search6789("timestamp", date)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    return search6789("sources", source)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    return search6789("categories", category)
