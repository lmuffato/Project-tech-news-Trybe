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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


print(search_by_title("Sherlock"))
