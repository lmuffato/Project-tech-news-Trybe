from tech_news.database import db


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    query = [
        {
            "$project": {
                "_id": 0,
                "title": 1,
                "url": 1,
                "total": {"$add": ["$shares_count", "$comments_count"]},
            },
        },
        {
            "$sort": {
                "total": -1,
                "title": 1,
            }
        }
    ]
    results = db.news.aggregate(query)
    return [(result["title"], result["url"]) for result in results][:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
