from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_result = find_news()

    most_popular_news = sorted(
        news_result,
        key=lambda news: news["shares_count"] +
        news["comments_count"], reverse=True)

    top_5 = []
    for news in most_popular_news:
        top_5.append((news["title"], news["url"]))
    return top_5[:5]


# Requisito 11
def top_5_categories():
    news_result = find_news()
    categories = []
    for new in news_result:
        for category in new["categories"]:
            categories.append(category)
    return sorted(categories)[:5]
