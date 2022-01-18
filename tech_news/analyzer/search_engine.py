import re
from tech_news.database import search_news


# Requisito 6
# Busca por regex no pymongo consultado no StackOverflow:
# https://stackoverflow.com/questions/3483318/performing-regex-queries-with-pymongo
def search_by_title(title):
    title_regex = re.compile(title, re.IGNORECASE)
    all_news = search_news({"title": title_regex})
    result = []
    for news in all_news:
        result.append((news["title"], news["url"]))
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
