from tech_news.database import search_news
from datetime import datetime

# Requisito 6


def search_by_title(title):
    """Seu código deve vir aqui"""
    # Obtem notícia salva no banco de acordo com o title
    result = []
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    for notice in data:
        titles = (notice["title"], notice["url"])
        result.append(titles)
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    # Obtem a notícia salva no banco de acordo com a data de publicação,
    # após verificar se a data informada tem o valor certo
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    result = []
    data = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    for notice in data:
        dates = (notice["title"], notice["url"])
        result.append(dates)
    return result


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
