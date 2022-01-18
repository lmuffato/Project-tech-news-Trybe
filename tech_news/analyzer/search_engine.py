import re
import datetime
from tech_news.database import search_news


# Requisito 6
# Busca por regex no pymongo consultado no StackOverflow:
# https://stackoverflow.com/questions/3483318/performing-regex-queries-with-pymongo
def search_by_title(title):
    title_regex = re.compile(title, re.IGNORECASE)
    all_news = search_news({"title": title_regex})
    result = []
    for news in all_news:
        result.append((news["title"], news["url"]))
    return result


# Requisito 7
# Validação da data consultada em:
# https://www.kite.com/python/answers/how-to-validate-a-date-string-format-in-python
def search_by_date(date):
    format = "%Y-%m-%d"
    try:
        datetime.datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Data inválida")

    date_regex = re.compile(date)
    all_news = search_news({"timestamp": date_regex})
    result = []
    for news in all_news:
        result.append((news["title"], news["url"]))
    return result


# Requisito 8
def search_by_source(source):
    source_regex = re.compile(source, re.IGNORECASE)
    all_news = search_news({"sources": source_regex})
    result = []
    for news in all_news:
        result.append((news["title"], news["url"]))
    return result


# Requisito 9
def search_by_category(category):
    category_regex = re.compile(category, re.IGNORECASE)
    all_news = search_news({"categories": category_regex})
    result = []
    for news in all_news:
        result.append((news["title"], news["url"]))
    return result
