from tech_news.database import db


def map_answer(news_list):
    return [(x["title"], x["url"]) for x in news_list]


# Requisito 10
def top_5_news():
    set1 = {
      "$set": {
        "popularity": {
          "$add": ["$shares_count", "$comments_count"]
        }
      }
    }
    sort1 = {
      "$sort": {
        "popularity": -1,
        "title": 1
      }
    }
    limit1 = {
      "$limit": 5
    }

    return map_answer(list(db.news.aggregate([set1, sort1, limit1])))


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
