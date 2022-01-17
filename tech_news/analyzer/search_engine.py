from datetime import datetime
from re import IGNORECASE, compile
from tech_news.database import search_news

# https://stackoverflow.com/questions/6266555
def search_text(field):
    def curried(value):
        news = search_news({ field: compile(value, IGNORECASE) })
        return list(map(lambda n: (n['title'], n['url']), news))
    return curried

# Requisito 6
def search_by_title(title):
    return search_text('title')(title)

# https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime
# Requisito 7
def search_by_date(timestamp):
    try:
        datetime.strptime(timestamp, "%Y-%m-%d")        
        return search_text('timestamp')(timestamp)
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_source(sources):
    return search_text('sources')(sources)


# Requisito 9
def search_by_category(categories):
    return search_text('categories')(categories)
