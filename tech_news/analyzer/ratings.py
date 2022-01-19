from tech_news.database import find_news


# Requisito 10
def popularity(new):
    return new["shares_count"] + new["comments_count"]


def top_5_news():
    news_list = find_news()
    if not news_list:
        return []

    news_list.sort(reverse=True, key=popularity)

    return [(new["title"], new["url"]) for new in news_list[:5]]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
