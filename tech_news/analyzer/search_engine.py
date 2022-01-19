from tech_news.database import search_news
import time


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    tech_news_tupla = []

    for news in news:
        tech_news_tupla.append((news["title"], news["url"]))

    return tech_news_tupla


# Requisito 7
def search_by_date(date):
    try:
        time.strptime(date, "%Y-%m-%d")
        news = search_news({"timestamp": {"$regex": date}})

        if news:
            for news in news:
                return [(news["title"], news["url"])]
        return []

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
