from ..database import find_news


# Requisito 10
# Ref https://github.com/tryber/sd-010-a-tech-news/pull/65/files
def top_5_news():
    results = find_news()
    results.sort(
        key=lambda new: (new["shares_count"] + new["comments_count"]),
        reverse=True
        )
    top_5 = results[:5]
    return [(news['title'], news['url']) for news in top_5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
