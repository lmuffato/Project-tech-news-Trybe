from tech_news.database import find_news


def total_calculate(new):
    return new["shares_count"] + new["comments_count"]


# Requisito 10
def top_5_news():
    news_list = find_news()
    if not news_list:
        return []

    news_list.sort(reverse=True, key=total_calculate)
    return [(new["title"], new["url"]) for new in news_list[:5]]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
