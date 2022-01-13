from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_list = find_news()
    result = []
    if news_list:
        for news in news_list:
            popularidade = 0
            popularidade += news["shares_count"]
            popularidade += news["comments_count"]
            news["popularidade"] = popularidade
    sorted_news = sorted(
        news_list, key=lambda i: (i['popularidade'], i['title']), reverse=True)
    index = 0
    for news in sorted_news:
        if index < 5:
            result.append((news["title"], news["url"]))
            index += 1
    return result
    """Seu código deve vir aqui"""


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
