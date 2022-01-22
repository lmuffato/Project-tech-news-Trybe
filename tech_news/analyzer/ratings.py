from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    news = find_news()
    if not news:
        return []
    news.sort(
        reverse=True,
        key=lambda new: new['shares_count'] + new['comments_count']
    )
    return [(new['title'], new['url']) for new in news[:5]]


# Requisito 11
def top_5_categories():
    news = find_news()
    categories = []
    if not news:
        return []
    for new in news:
        categories.extend([*new['categories']])
    categories_count = Counter(categories)
    sorted_by_popularity = sorted(
        categories_count, key=categories_count.get, reverse=True
    )
    return sorted(sorted_by_popularity)[:5]
