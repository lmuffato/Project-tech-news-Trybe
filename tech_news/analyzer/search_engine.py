import tech_news.database as database
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
    format_date = datetime.strptime(date, "%Y-%m-%d")
    format_datetime = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    news = database.search_news()
    return [
            (report['title'], report['url'])
            for report in news
            if datetime.strptime(date, format_date).date()
            == datetime.strptime(report['timestamp'], format_datetime).date()
        ]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
