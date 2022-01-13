from tech_news.database import search_news
import re


def tuple_of_title_url_from_dict(news, title):
    return [tuple((new['title'], new['url']))
            for new in news
            if new['title'].lower() == title.lower()]

def create_new_regex_ignore_case(value):
    return re.compile(f'^{value}', re.IGNORECASE)


def search_by_title(title):
    reg = create_new_regex_ignore_case(title)
    news = search_news({'title': reg})
    titles = tuple_of_title_url_from_dict(news, title)

    if(not titles):
        return []
    return titles


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
