from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    title = search_news({"title": {"$regex": title, "$options": "i"}})
    info_list = []
    for news in title:
        selected_news = (news["title"], news["url"])
        info_list.append(selected_news)

    return info_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
