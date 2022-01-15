from ..database import find_news


# Requisito 10
def top_5_news():
    all_news = find_news()
    all_news.sort(
        key=lambda new: (new["shares_count"] + new["comments_count"]),
        reverse=True
        )
    top_5 = all_news[:5]
    return [(news['title'], news['url']) for news in top_5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
