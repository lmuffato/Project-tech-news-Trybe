from tech_news.database import db, find_news
from collections import Counter


# Requisito 10
def top_5_news():
    news = list(
        db.news.aggregate(
            [
                {
                    "$sort": {
                        "comments_count": -1,
                        "shares_count": -1,
                        "title": 1,
                    }
                },
                {"$limit": 5},
                {"$project": {"title": 1, "_id": 0, "url": 1}},
            ]
        )
    )
    titles_and_urls = [(new["title"], new["url"]) for new in news]
    return titles_and_urls


# Requisito 11
def top_5_categories():
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
