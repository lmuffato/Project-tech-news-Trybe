from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    if not news:
        return []
    news.sort(
        reverse=True,
        key=lambda new: new["shares_count"] + new["comments_count"]
    )
    return [(new["title"], new["url"]) for new in news[:5]]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
