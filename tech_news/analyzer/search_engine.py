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
    arr_news = search_news({"sources": {"$regex": source, "$options": "i"}})
    return [(news["title"], news["url"]) for news in arr_news]


# Requisito 9
def search_by_category(category):
    arr_news = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    return [(news["title"], news["url"]) for news in arr_news]
