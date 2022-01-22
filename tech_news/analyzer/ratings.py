from tech_news.database import find_news


# Requisito 10
def top_5_news():
    arr_news = find_news()

    arr_news.sort(
        reverse=True,
        key=lambda news: news['shares_count'] + news['comments_count']
    )
    return [(news['title'], news['url']) for news in arr_news[:5]]


# Requisito 11
def top_5_categories():
    arr_news = find_news()
    categories = []

    for news in arr_news:
        for category in news["categories"]:
            categories.append(category)

    return sorted(categories)[:5]
