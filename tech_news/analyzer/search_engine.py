from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query_capitalized = {'title': title.capitalize()}
    query_lowered = {'title': title.lower()}
    news = (
        search_news(query_lowered)
        or search_news(query_capitalized)
    )
    news_tuple = [(new['title'], new['url']) for new in news]
    return news_tuple


# Requisito 7
def search_by_date(date):
    try:
        # https://github.com/tryber/sd-010-a-tech-news/pull/64/files
        # https://docs.python.org/pt-br/3/library/datetime.html#strftime-and-strptime-behavior
        datetime.strptime(date, '%Y-%m-%d')
        query = {'timestamp': {'$regex': date}}
        news = search_news(query)
        news_tuple = [(new['title'], new['url']) for new in news]
        return news_tuple
    except ValueError:
        raise(ValueError('Data inválida'))


# Requisito 8
def search_by_source(source):
    query = {'sources': {"$regex": source, "$options": "i"}}
    news = search_news(query)
    news_tuple = [(new['title'], new['url']) for new in news]
    return news_tuple


# Requisito 9
def search_by_category(category):
    query = {'categories': {"$regex": category, "$options": "i"}}
    news = search_news(query)
    news_tuple = [(new['title'], new['url']) for new in news]
    return news_tuple
