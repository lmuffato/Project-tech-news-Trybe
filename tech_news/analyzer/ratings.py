from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    for n in news:
        n['rating'] = n['shares_count'] + n['comments_count']

    sorted_news = sorted(news, key=lambda d: (-d['rating'], d['title']))

    return [(n['title'], n['url']) for n in sorted_news][0:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
