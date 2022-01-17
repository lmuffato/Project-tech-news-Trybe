from ..database import search_news
from datetime import datetime
import re


# Requisito 6
def search_by_title(title):
    found_news = search_news({"title": re.compile(title, re.IGNORECASE)})
    return [(item["title"], item["url"]) for item in found_news]


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    found_news = search_news({"timestamp": {"$regex": date}})
    return [(item["title"], item["url"]) for item in found_news]


# Requisito 8
def search_by_source(source):
    found_news = search_news({"sources": re.compile(source, re.IGNORECASE)})
    return[(item["title"], item["url"]) for item in found_news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
