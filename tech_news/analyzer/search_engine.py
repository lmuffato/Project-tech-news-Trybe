from tech_news.database import find_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = find_news()
    news_filtered = []
    for article in news:
        if article["title"].lower() == title.lower():
            news_filtered.append(article)
    return [(news["title"], news["url"]) for news in news_filtered]


def validate_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 7
def search_by_date(date):
    if type(date) == str:
        validate_date(date)
        news = find_news()
        news_filtered = []
        for article in news:
            if date in article["timestamp"]:
                news_filtered.append(article)
        return [(news["title"], news["url"]) for news in news_filtered]
    else:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = find_news()
    news_filtered = []
    for article in news:
        for sources in article["sources"]:
            if sources.lower() == source.lower():
                news_filtered.append(article)
    return [(news["title"], news["url"]) for news in news_filtered]


# Requisito 9
def search_by_category(category):
    news = find_news()
    news_filtered = []
    for article in news:
        for category_item in article["categories"]:
            if category_item.lower() == category.lower():
                if article not in news_filtered:
                    news_filtered.append(article)
    return [(news["title"], news["url"]) for news in news_filtered]
