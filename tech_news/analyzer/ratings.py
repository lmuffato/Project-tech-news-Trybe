from ..database import find_news
from collections import Counter


# Requisito 10
# Ref https://github.com/tryber/sd-010-a-tech-news/pull/65/files
def top_5_news():
    results = find_news()
    results.sort(
        key=lambda new: (new["shares_count"] + new["comments_count"]),
        reverse=True,
    )
    top_5 = results[:5]
    return [(news["title"], news["url"]) for news in top_5]


# Requisito 11
def top_5_categories():
    results = find_news()
    categories = []

    if not results:
        return []

    for notice in results:
        categories.append(notice["categories"])

    count = Counter(categories)
    sorted_list = sorted(count, key=count.get, reverse=True)
    return sorted(sorted_list)[:5]
