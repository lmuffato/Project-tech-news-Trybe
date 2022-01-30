from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query_capitalized = {'title': title.capitalize()}
    query_lowered = {'title': title.lower()}
    news = (
        search_news(query_lowered)
        or search_news(query_capitalized)
    )
    news_tuple = [(new['title'], new['url']) for new in news]
    return news_tuple


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
