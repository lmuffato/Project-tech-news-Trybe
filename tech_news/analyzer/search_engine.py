from tech_news.database import search_news
import re
import datetime


# Requisito 6
def search_by_title(title):
    # https://stackoverflow.com/questions/3483318/performing-regex-queries-with-pymongo
    regx = re.compile(f".*{title}.*", re.IGNORECASE)
    found_news = search_news({"title": regx})
    list = []
    for news in found_news:
        list.append((news["title"], news["url"]))
    return list


# Requisito 7
def search_by_date(date):
    # https://stackoverflow.com/questions/50504500/deprecationwarning-invalid-escape-sequence-what-to-use-instead-of-d
    date_pattern = r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[1-9]|3[0-1])"
    date_match = re.match(date_pattern, date)
    if not date_match:
        raise ValueError("Data inválida")
    date_splitted = date.split("-")
    year = int(date_splitted[0])
    month = int(date_splitted[1])
    day = int(date_splitted[2])
    try:
        datetime.datetime(year, month, day)
    except ValueError:
        raise ValueError("Data inválida")

    found_news = search_news({"timestamp": re.compile(f"{date}.*")})
    list = []
    for news in found_news:
        list.append((news["title"], news["url"]))
    return list


# Requisito 8
def search_by_source(source):
    found_news = search_news({"sources": re.compile(source, re.IGNORECASE)})
    list = []
    for news in found_news:
        list.append((news["title"], news["url"]))
    return list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
