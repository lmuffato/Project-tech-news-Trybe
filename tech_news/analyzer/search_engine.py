from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_by_title = search_news({'title': {'$regex': title, '$options': 'i'}})
    return [(n['title'], n['url']) for n in news_by_title]


# Requisito 7
def search_by_date(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')
    except ValueError:
        raise ValueError('Data inválida')

    news_by_date = search_news({'timestamp': {'$regex': date}})
    return [(n['title'], n['url']) for n in news_by_date]


# Requisito 8
def search_by_source(source):
    news_by_source = search_news(
        {'sources': {'$regex': source, '$options': 'i'}}
    )
    return [(n['title'], n['url']) for n in news_by_source]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
