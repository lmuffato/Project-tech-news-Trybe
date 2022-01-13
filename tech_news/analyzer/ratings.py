from tech_news.database import db, client


# Requisito 10
def top_5_news():
    top_list = []

    with client:
        for new in db.news.aggregate([
          {"$addFields": {"sort_order": {
            "$add": ["$shares_count", "$comments_count"]
          }}},
          {"$sort": {"sort_order": -1}},
          {"$project": {"sort_order": 0}},
          {"$limit": 5}
          ]):

            top_list.append((new["title"], new["url"]))

    return top_list

# Foi consultado os seguintes links para resolução:
# https://docs.mongodb.com/manual/reference/operator/aggregation/limit/
# https://stackoverflow.com/questions/48786941/how-to-sort-with-the-sum-of-2-fields-in-mongodb


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
