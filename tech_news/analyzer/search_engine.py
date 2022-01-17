import tech_news.database as db
from datetime import datetime
from .validation_date import validation_date, format_date, format_datetime


# Requisito 6
def search_by_title(title):
    news = db.find_news()

    return [
        (report['title'], report['url'])
        for report in news
        if title.lower() in report['title'].lower()
    ]


# Requisito 7
def search_by_date(date):
    validation_date(date)
    news = db.find_news()
    return [
        (report['title'], report['url'])
        for report in news
        if datetime.strptime(date, format_date).date()
        == datetime.strptime(report['timestamp'], format_datetime).date()
    ]


# Requisito 8
def search_by_source(source):
    news = db.find_news()
    return [
        (report['title'], report['url'])
        for report in news
        if source.lower()
        in (sources.lower() for sources in report['sources'])
    ]


# Requisito 9
def search_by_category(category):
    news = db.find_news()
    return [
        (report['title'], report['url'])
        for report in news
        if category.lower()
        in (categories.lower() for categories in report['categories'])
    ]
