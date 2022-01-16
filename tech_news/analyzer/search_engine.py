from datetime import datetime
import re
from tech_news.database import search_news

# Visto o repositório do Alexandre Oliveira que esclareceu como
# realizar estas atividades


# Requisito 6
def search_by_title(title):
    titles = search_news({
        "title": re.compile(title, re.IGNORECASE)})
    if (len(titles)):
        return [(new["title"], new["url"]) for new in titles]
    else:
        return []


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    dates = search_news({"timestamp": {"$regex": date}})
    if (len(dates)):
        return [(new["title"], new["url"]) for new in dates]
    else:
        return []


# Requisito 8
def search_by_source(source):
    sources = search_news({
        "sources": re.compile(source, re.IGNORECASE)})
    if (len(sources)):
        return [(new["title"], new["url"]) for new in sources]
    else:
        return []


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
