from datetime import datetime
from tech_news.database import search_news


# https://pt.stackoverflow.com/questions/496212/fazer-uma-consulta-com-pymongo-filtrando-por-uma-string-ignorando-letras-maiuscu
# Requisito 6
def search_by_title(title):
    news_by_title = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_by_title]


# print(search_by_title(""))


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        news_by_date = search_news(
            {"timestamp": {"$regex": date, "$options": "i"}})
        return [(news["title"], news["url"]) for news in news_by_date]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news_by_sources = search_news({"sources": {"$regex": source, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_by_sources]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
