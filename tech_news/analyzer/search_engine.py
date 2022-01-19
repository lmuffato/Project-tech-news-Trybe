from tech_news.database import search_news
import re
import time


# Requisito 6
def search_by_title(title):
    news = search_news({"title": re.compile(title, re.IGNORECASE)})
    return [(new["title"], new["url"]) for new in news]


# Requisito 7
def search_by_date(date):
    try:
        time.strptime(date, "%Y-%m-%d")
        news = search_news({"timestamp": re.compile(date)})
        return [(new["title"], new["url"]) for new in news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = search_news({"sources": re.compile(source, re.IGNORECASE)})
    return [(new["title"], new["url"]) for new in news]


# Requisito 9
def search_by_category(category):
    news = search_news({"categories": re.compile(category, re.IGNORECASE)})
    return [(new["title"], new["url"]) for new in news]
