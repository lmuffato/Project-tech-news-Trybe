from tech_news.database import search_news
import time

# Requisito 6
def search_by_title(title):
    arr_news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news['title'], news['url']) for news in arr_news]


# Requisito 7
def search_by_date(date):
    try:
        time.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    arr_news = search_news({"timestamp": {"$regex": date}})
    return [(news["title"], news["url"]) for news in arr_news]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
