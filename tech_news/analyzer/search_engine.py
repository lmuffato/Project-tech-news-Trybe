from tech_news.database import search_news
import time


# REQUISITO 6
def search_by_title(title):
    fetch_by_title = search_news({"title": {"$regex": title, "$options": "i"}})
    fetch_result = []
    for news in fetch_by_title:
        found_note = (news["title"], news["url"])
        fetch_result.append(found_note)

    return fetch_result


# REQUISITO 7
def search_by_date(date):
    try:
        time.strptime(date, "%Y-%m-%d")
        fetch_by_date = search_news({"timestamp": {"$regex": date}})
        fetch_result = []
        for news in fetch_by_date:
            found_note = (news["title"], news["url"])
            fetch_result.append(found_note)

        return fetch_result

    except ValueError:
        raise ValueError("Data inválida")


# REQUISITO 8
def search_by_source(source):
    fetch_by_source = search_news(
        {"sources": {"$regex": source, "$options": "i"}})

    fetch_result = []
    for news in fetch_by_source:
        found_note = (news["title"], news["url"])
        fetch_result.append(found_note)

    return fetch_result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
