from ..database import find_news


# Requisito 10
def top_5_news():
    data = find_news()
    news = []

    data.sort(
        key=lambda item: (item["shares_count"] + item["comments_count"]),
        reverse=True,
    )

    for item in data[:5]:
        noticia = (item["title"], item["url"])
        news.append(noticia)

    return news


# Requisito 11
def top_5_categories():
    data = find_news()
    categories = {}

    for item in data:
        for category in item["categories"]:
            if category in categories:
                categories[category] += 1
            else:
                categories[category] = 1

    keys = categories.keys()

    result = sorted(
        keys, key=lambda category: (categories[category], category)
    )

    return result[:5]
