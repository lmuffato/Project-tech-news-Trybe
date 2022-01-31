from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    list = find_news()
    if not list:
        return []
    list.sort(
        reverse=True,
        key=lambda new: new["shares_count"] + new["comments_count"],
    )
    return [(new["title"], new["url"]) for new in list[:5]]


# Requisito 11
def top_5_categories():
    list = find_news()
    categories = []
    if not list:
        return []
    for gokuSsj in list:
        categories.extend([*gokuSsj["categories"]])
    cont = Counter(categories)
    sort = sorted(cont, key=cont.get, reverse=True)
    return sorted(sort)[:5]
