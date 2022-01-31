# Requisito 10
from database import find_news
from collections import Counter


def top_5_news():
    """Seu código deve vir aqui"""
    news_list = find_news()
    if not news_list:
        return []
    news_list.sort(
        reverse=True,
        key=lambda new: new['shares_count'] + new['comments_count']
    )
    return [(new['title'], new['url']) for new in news_list[:5]]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    news_list = find_news()
    categories = []
    if not news_list:
        return []
    for new in news_list:
        categories.extend([*new['categories']])
    cont = Counter(categories)
    sorted_by_popularity = sorted(
        cont, key=cont.get, reverse=True
    )
    return sorted(sorted_by_popularity)[:5]
