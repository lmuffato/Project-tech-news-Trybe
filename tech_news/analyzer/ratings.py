from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    cmnts = 'comments_count'
    shares = 'shares_count'
    tops = sorted([
        (new[cmnts] + new[shares], new['title'], new['url']) for new in news
    ], reverse=True)
    tops_5 = []
    for n in range(len(tops)):
        if n > 4:
            break
        new = tops[n]
        tops_5.append((new[1], new[2]))
    return tops_5



# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
