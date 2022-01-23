from tech_news.database import db


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
    categories = db.news.aggregate(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
            {"$sort": {"count": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )
    top_5 = sorted(list(category["_id"] for category in categories))
    return top_5
