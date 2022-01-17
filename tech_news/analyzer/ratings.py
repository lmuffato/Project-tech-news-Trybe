from tech_news.database import find_news


# Requisito 10
def top_5_news():
    all_ns = find_news()
    sn = sorted(all_ns, key=lambda k: -k["comments_count"] - k["shares_count"])
    top_5 = sn[0:5]
    return [(news["title"], news["url"]) for news in top_5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
