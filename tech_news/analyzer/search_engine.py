import tech_news.database as db


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = db.search_news({
        "title": {
            "$regex": title,
            "$options": "i",
        },
    })
    to_return = []
    for new in news:
        to_return.append((new["title"], new["url"]))
    
    return to_return


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
