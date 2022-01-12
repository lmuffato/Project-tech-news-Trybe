from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    news = find_news()
    news_filtered = []
    for article in news:
        if article["title"].lower() == title.lower():
            news_filtered.append(article)
    return [(news["title"], news["url"]) for news in news_filtered]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
