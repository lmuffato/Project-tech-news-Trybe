from tech_news.database import search_news
import re


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = []
    db_news = search_news({"title": {"$regex": title, "$options": "i"}})
    for notice in db_news:
        news.append((notice["title"], notice["url"]))
    return news

# https://docs.mongodb.com/manual/reference/operator/query/regex/


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    print("print da data no inicio", date, type(date))
    news = []
    validate = re.search(r"\d{4}-\d{2}-\d{2}", date)
    data_dia = date.split("-")[-1]
    data_mes = date.split("-")[1]
    valida_data_nao_existente = True
    if (data_mes == "02" and int(data_dia) > 29) or int(data_mes) > 12:
        valida_data_nao_existente = None
    if validate is None or valida_data_nao_existente is None:
        raise ValueError("Data inválida")
    db_news = search_news(
        {"timestamp": {"$regex": date, "$options": "i"}})
    for notice in db_news:
        news.append((notice["title"], notice["url"]))
    return news


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news = []
    db_news = search_news({"sources": {"$regex": source, "$options": "i"}})
    for notice in db_news:
        news.append((notice["title"], notice["url"]))
    return news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
