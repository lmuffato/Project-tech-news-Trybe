from tech_news.database import find_news
# https://docs.python.org/3/library/collections.html
from collections import Counter


# Requisito 10
def top_5_news():
    news = find_news()
    cmnts = 'comments_count'
    shares = 'shares_count'
    tops = sorted([
        (new[cmnts] + new[shares], new['title'], new['url']) for new in news
    ], reverse=True)
    top_5 = []
    for n in range(len(tops)):
        if n > 4:
            break
        new = tops[n]
        top_5.append((new[1], new[2]))
    return top_5


def get_sorted_categories(categories):
    categories_counter = []
    for category, value in categories.items():
        categories_counter.append((value, category))
    return sorted(categories_counter)


# Requisito 11
def top_5_categories():
    news = find_news()
    categories = []

    for new in news:
        categories.extend(new['categories'])

    counters = Counter(categories)
    categories_sorted = get_sorted_categories(counters)
    top_5 = []
    for n in range(len(categories_sorted)):
        if n > 4:
            break
        category = categories_sorted[n]
        top_5.append(category[1])

    return top_5
