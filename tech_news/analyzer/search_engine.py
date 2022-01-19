from tech_news.database import search_news


# REQUISITO 6
def search_by_title(title):
    fetch_by_title = search_news({"title": {"$regex": title, "$options": "i"}})
    fetch_result = []
    for news in fetch_by_title:
        found_note = (news["title"], news["url"])
        fetch_result.append(found_note)

    return fetch_result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
