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
    news = find_news()

    categories_count = {}
    for n in news:
        for cat in n['categories']:
            if cat not in categories_count:
                categories_count[cat] = 1
            else:
                categories_count[cat] += 1

    sorted_tuples = [
        c[0] for c in
        sorted(categories_count.items(), key=lambda item: (item[1], item[0]))
    ]

    return sorted_tuples[0:5]
