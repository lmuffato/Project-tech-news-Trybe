from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    all_ns = find_news()
    sn = sorted(all_ns, key=lambda k: -k["comments_count"] - k["shares_count"])
    top_5 = sn[0:5]
    return [(news["title"], news["url"]) for news in top_5]


# Requisito 11
def top_5_categories():
    all_ns = find_news()
    categories = []
    for news in all_ns:
        categories += [*news["categories"]]
    quantities = Counter(categories)
    sorted_categories = []
    for i in sorted(quantities, key=quantities.get):
        sorted_categories.append(i)
    return sorted(sorted_categories)[0:5]
