from tech_news.database import find_news
from collections import Counter


def total_calculate(new):
    return new["shares_count"] + new["comments_count"]


# Requisito 10
def top_5_news():
    news_list = find_news()
    if not news_list:
        return []

    news_list.sort(reverse=True, key=total_calculate)
    return [(new["title"], new["url"]) for new in news_list[:5]]


# Requisito 11
def top_5_categories():
    news_list = find_news()
    categories = []
    if not news_list:
        return []
    for new in news_list:
        categories.extend([*new['categories']])
    counter = Counter(categories)
    total_sort = sorted(
        counter, key=counter.get, reverse=True
    )

    return sorted(total_sort)[:5]
