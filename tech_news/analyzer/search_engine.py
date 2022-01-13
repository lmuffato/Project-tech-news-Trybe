import datetime
from tech_news.database import db
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = {"title": {'$regex': title, '$options': 'i'}}
    options = {"title": 1, "url": 1, "_id": 0}
    news_dict = list(db.news.find(query, options))
    tuplas_news = []

    for n in news_dict:
        tuplas_news.append((n["title"], n["url"]))

    return tuplas_news


# Requisito 7
# Código da validação da data:
# https://qastack.com.br/programming/16870663/how-do-i-validate-a-date-string-format-in-python
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        query = {"timestamp": {'$regex': date, '$options': 'i'}}
        news_dict = search_news(query)
        tuplas_news = []

        for n in news_dict:
            tuplas_news.append((n["title"], n["url"]))

        return tuplas_news
    except ValueError:
        raise ValueError("Data inválida")

# print(search_by_date('2022-01-13'))


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
