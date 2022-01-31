from tech_news.database import find_news


# Requisito 10
def top_5_news():
    list = find_news()
    if not list:
        return []
    list.sort(
        reverse=True,
        key=lambda new: new["shares_count"] + new["comments_count"],
    )
    return [(new["title"], new["url"]) for new in list[:5]]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
