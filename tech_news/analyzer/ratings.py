from tech_news.database import find_news


# Requisito 10
def top_5_news():
    get_news = find_news()
    top_five = []

    most_popular_news = sorted(
        get_news,
        key=lambda news: news["shares_count"] +
        news["comments_count"], reverse=True
    )

    for news in most_popular_news:
        top_five.append((news["title"], news["url"]))

    return top_five[:5]

    # Referências para fazer requisito 10:
    # https://github.com/tryber/sd-010-a-tech-news/blob/rodolfo-oliveira-tech-news/tech_news/analyzer/ratings.py
    # https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda


# Requisito 11
def top_5_categories():
    news = find_news()
    categories = []

    for news in news:
        for category in news["categories"]:
            categories.append(category)

    return sorted(categories)[:5]
