from tech_news.database import search_news
import time


# Requisito 6
def search_by_title(title):
    news = search_news({'title': {'$regex': title, '$options': 'i'}})
    return [(new['title'], new['url']) for new in news]


# Requisito 7
def search_by_date(date):
    try:
        time.strptime(date, '%Y-%m-%d')
        news = search_news({'timestamp': {'$regex': date, '$options': 'i'}})
        return [(new['title'], new['url']) for new in news]
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_source(source):
    news = search_news({'sources': {'$regex': source, '$options': 'i'}})
    return [(new['title'], new['url']) for new in news]


# Requisito 9
def search_by_category(category):
    news = search_news({'categories': {'$regex': category, '$options': 'i'}})
    return [(new['title'], new['url']) for new in news]
