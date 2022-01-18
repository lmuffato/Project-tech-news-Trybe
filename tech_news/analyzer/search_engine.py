from tech_news.database import search_news
from time import strptime


# Requisito 6
def search_by_title(title):
    find_by_title = search_news({"title": {"$regex": title, "$options": "i"}})
    find_result = []
    for news in find_by_title:
        found_note = (news["title"], news["url"])
        find_result.append(found_note)

    return find_result


# Requisito 7
def search_by_date(date):
    try:
        strptime(date, "%Y-%m-%d")
        find_by_date = search_news({"timestamp": {"$regex": date}})
        find_result = []
        for news in find_by_date:
            found_note = (news["title"], news["url"])
            find_result.append(found_note)

        return find_result

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    find_by_source = search_news(
        {"sources": {"$regex": source, "$options": "i"}})

    find_result = []
    for news in find_by_source:
        found_note = (news["title"], news["url"])
        find_result.append(found_note)

    return find_result


# Requisito 9
def search_by_category(category):
    find_by_category = search_news(
        {"categories": {"$regex": category, "$options": "i"}})

    find_result = []
    for news in find_by_category:
        found_note = (news["title"], news["url"])
        find_result.append(found_note)

    return find_result
