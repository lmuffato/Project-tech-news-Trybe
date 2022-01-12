from tech_news.database import search_news
import re


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    # https://www.tutorialspoint.com/How-to-write-a-case-insensitive-Python-regular-expression-without-re-compile
    search_title = []
    news = search_news({"title": re.compile(title, re.IGNORECASE)})
    # print(news)
    for new in news:
        search_title.append((new["title"], new["url"]))
    print(search_title)
    return search_title


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
