from tech_news.database import search_news
from time import strptime


# Requisito 6
def search_by_title(title):
    query = {
        'title': {
            '$regex': title,
            '$options': 'i',
        }
    }
    results = search_news(query)
    news = [(result['title'], result['url']) for result in results]
    return news


# Requisito 7
def search_by_date(date):
    date_format = '%Y-%m-%d'
    try:
        strptime(date, date_format)
    except ValueError:
        raise ValueError('Data inválida')
    query = {
        'timestamp': {
            '$regex': date
        }
    }
    results = search_news(query)
    news = [(result['title'], result['url']) for result in results]
    return news


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
