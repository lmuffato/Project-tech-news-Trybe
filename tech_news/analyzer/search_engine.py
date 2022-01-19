from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    find_news = search_news({"title": {"$regex": title, "$options": "i"}})
    list_news = []

    for news in find_news:
        result = (news["title"], news["url"])
        list_news.append(result)

    return list_news


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    find_news = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    list_news = []

    for news in find_news:
        result = (news["title"], news["url"])
        list_news.append(result)

    return list_news


# Requisito 8
def search_by_source(source):
    find_news = search_news({"sources": {"$regex": source, "$options": "i"}})
    list_news = []

    for news in find_news:
        result = (news["title"], news["url"])
        list_news.append(result)

    return list_news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


print(search_by_title("Sherlock"))
print(search_by_date("2022-01-18"))
print("busca por source")
print(search_by_source("Screen Rant"))
