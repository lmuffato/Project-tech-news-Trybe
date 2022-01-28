from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    table = find_news()
    table = [
           (
                item["title"],
                item["url"],
                item["shares_count"] + item["comments_count"],
           )
           for item in table
    ]
    sorted_table = sorted(table, key=lambda item: item[2], reverse=True)[:5]
    sorted_table = [(item[0], item[1]) for item in sorted_table]
    return sorted_table


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    table = find_news()
    categories = [cat for item in table for cat in item["categories"]]
    sorted_categories = sorted(
        sorted(
            categories,
            key=lambda x: -categories.count(x),
            reverse=True)
        )[:5]

    return sorted_categories
