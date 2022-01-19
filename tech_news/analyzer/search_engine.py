import tech_news.database as database
from tech_news.database import search_news
from datetime import datetime


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
    except ValueError:
        raise ValueError("Data inválida")
    news = search_news({"timestamp": {"$regex": date}})
    return [(item["title"], item["url"]) for item in news]
    # Src: pr de felipe flores - teste


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
