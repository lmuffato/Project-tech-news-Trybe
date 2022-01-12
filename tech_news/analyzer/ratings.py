from ..database import db


# Requisito 10
def top_5_news():
    sorted_data = db.news.aggregate([
        {
            "$addFields": {
                "popularity": {"$add": ["$comments_count", "$shares_count"]}
            }
        },
        {"$sort": {"popularity": -1}},
        {"$limit": 5}
    ])

    return [
        (news['title'], news['url'])
        for news in sorted_data
    ]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
