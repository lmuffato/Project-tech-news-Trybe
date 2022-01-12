from tech_news.database import search_news
import re


# Requisito 6
def search_by_title(title):
    # https://stackoverflow.com/questions/3483318/performing-regex-queries-with-pymongo
    regx = re.compile(f".*{title}.*", re.IGNORECASE)
    found_news = search_news({"title": regx})
    list = []
    for news in found_news:
        list.append((news["title"], news["url"]))
    return list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
