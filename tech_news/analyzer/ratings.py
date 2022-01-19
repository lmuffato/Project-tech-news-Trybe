from tech_news.database import find_news


def popularity(new):
    return new["shares_count"] + new["comments_count"]


# Requisito 10
def top_5_news():
    # """Seu código deve vir aqui"""
    news = find_news()
    if not news:
        return []
    news.sort(reverse=True, key=popularity)
    return [(new["title"], new["url"]) for new in news[:5]]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
