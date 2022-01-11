from tech_news.database import find_news
import collections


def calculate_popularity(new):
    return new["shares_count"] + new["comments_count"]


# Requisito 10
def top_5_news():
    news = find_news()
    if not news:
        return []

    news.sort(reverse=True, key=calculate_popularity)

    return [(new["title"], new["url"]) for new in news[:5]]


# Requisito 11
def top_5_categories():
    news = find_news()
    if not news:
        return []

    categories = []
    for new in news:
        categories = [*categories, *new["categories"]]
    most_commons = list(collections.Counter(categories))
    return [category for category in sorted(most_commons)[:5]]
