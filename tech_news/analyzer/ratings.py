# Requisito 10
from tech_news.database import find_news
from collections import Counter


def top_5_news():
    """Seu código deve vir aqui"""
    data = find_news()
    result = []

    data.sort(
        key=lambda news: (news["shares_count"] + news["comments_count"]),
        reverse=True
    )

    for item in data[:5]:
        new = (item["title"], item["url"])
        result.append(new)

    return result

# Ref:
# https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    data = find_news()
    result = []

    if not data:
        return []

    for item in data:
        result.extend([*item["categories"]])
        qty_categories = Counter(result)
        by_popularity = sorted(
            qty_categories, key=qty_categories.get, reverse=True
        )

    return sorted(by_popularity)[:5]
