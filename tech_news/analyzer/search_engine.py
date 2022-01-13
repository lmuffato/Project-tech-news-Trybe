from datetime import datetime
from tech_news.database import search_news
import re


def tuple_from_dict(news, search_param, search_param_str):
    return [tuple((new['title'], new['url']))
            for new in news
            if search_param.lower() in new[search_param_str].lower()]


def create_new_regex_ignore_case(value):
    return re.compile(f'^{value}', re.IGNORECASE)


def exists(value):
    if(not value):
        return []
    else:
        return value


def search_by_title(title):
    reg = create_new_regex_ignore_case(title)
    news = search_news({'title': reg})
    titles = tuple_from_dict(news, title, 'title')

    return exists(titles)


def validate_date(date_str):
    try:
        date_format = '%Y-%m-%d'
        datetime.strptime(date_str, date_format)
    except ValueError:
        raise ValueError('Data inválida')


def search_by_date(date):
    validate_date(date)
    news = search_news({'timestamp': {'$regex': date}})
    dates = tuple_from_dict(news, date, 'timestamp')
    return exists(dates)


def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
