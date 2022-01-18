import tech_news.database as database


# Requisito 6
def search_by_title(title):
    # """Seu código deve vir aqui"""
    news = database.find_news()

    return [
        (report['title'], report['url'])
        for report in news
        if title.lower() in report['title'].lower()
    ]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
