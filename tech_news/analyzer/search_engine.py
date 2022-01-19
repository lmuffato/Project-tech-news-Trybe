import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    # Regex:
    # https://trybecourse.slack.com/archives/C016CCMKN9E/p1621460054120000?thread_ts=1621457890.115800&cid=C016CCMKN9E
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    # Validar formato de data
    # https://qastack.com.br/programming/16870663/how-do-i-validate-a-date-string-format-in-python
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    news = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news = search_news({"sources": {"$regex": source, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    news = search_news({"categories": {"$regex": category, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]
