from datetime import datetime
from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    db_list = find_news()
    filtered_news = []
    for news in db_list:
        if news["title"].upper() == title.upper():
            filtered_news.append(news)
    return [(news["title"], news["url"]) for news in filtered_news]


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        db_list = find_news()
        filtered_news = []
        for news in db_list:
            if date in news["timestamp"]:
                filtered_news.append(news)
        return [(news["title"], news["url"]) for news in filtered_news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    db_list = find_news()
    filtered_news = []
    for news in db_list:
        for fonte in news["sources"]:
            if fonte.upper() == source.upper():
                filtered_news.append(news)
    return [(news["title"], news["url"]) for news in filtered_news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
