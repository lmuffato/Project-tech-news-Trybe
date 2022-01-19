import tech_news.database as database
from datetime import datetime
import re


# Requisito 6
def search_by_title(title):
    # """Seu código deve vir aqui"""
    news = database.find_news()

    return [
        (report['title'], report['url'])
        for report in news
        if title.lower() in report['title'].lower()
    ]


# Requisito 7
def search_by_date(date):
    # """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        res = database.search_news({"timestamp": re.compile(date)})
        # re - Regular expression - forma de regex utilizada em python:
        # src https://www.hashtagtreinamentos.com/regular-expressions-no-python 
        news = []
        if res:
            for noticia in res:
                news.append((noticia["title"], noticia["url"]))
            return news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    # """Seu código deve vir aqui"""
    news = database.find_news()
    return [
        (report['title'], report['url'])
        for report in news
        if source.lower()
        in (sources.lower() for sources in report['sources'])
    ]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    news = database.find_news()
    return [
        (report['title'], report['url'])
        for report in news
        if category.lower()
        in (categories.lower() for categories in report['categories'])
    ]
