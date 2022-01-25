from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    db_list = find_news()
    filtered_news = []
    for news in db_list:
        if news["title"].upper() == title.upper():
            print(f'\n noticia {news}')
            filtered_news.append(news)
    return [(news["title"], news["url"]) for news in filtered_news]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
