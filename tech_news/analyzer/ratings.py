from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    news_list = []
    response = find_news()
    if len(response) == 0:
        return response
    for item in response:
        news_dicts = {
            "title": item["title"],
            "url": item["url"],
            "popularity": item["comments_count"] + item["shares_count"],
        }
        news_list.append(news_dicts)

    sorted_news = sorted(
        news_list, key=lambda k: (k["popularity"], k["title"]), reverse=True
    )
    news_list_ordered = []
    for news_ordered in sorted_news:
        news_typle = news_ordered["title"], news_ordered["url"]
        news_list_ordered.append(news_typle)
    return news_list_ordered[:5]


# Requisito 11
def top_5_categories():
    news_list = []
    response = find_news()
    if len(response) == 0:
        return response
    for item in response:
        for cat in item["categories"]:
            news_list.append(cat)
    duplicates = Counter(news_list)
    top_typle = duplicates.most_common()
    categories_list = []
    for category in top_typle:
        categories_list.append(category[0])
    categories_list.sort()
    top_5_list = categories_list[:5]
    return top_5_list
