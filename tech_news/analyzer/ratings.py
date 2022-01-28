from tech_news.database import find_news
from collections import Counter


def popular_news():
    pop_list = []
    db_news = find_news()
    count_pop = 0
    for news in db_news:
        count_pop = news["comments_count"] + news["shares_count"]
        pop_list.append(
            {"title": news["title"], "url": news["url"], "pop": count_pop}
        )
    print(count_pop)
    return pop_list


# Requisito 10
def top_5_news():
    sorted_list = popular_news()
    sorted(sorted_list, key=lambda tup: ([2]), reverse=True)
    response = []
    for news in sorted_list[:5]:
        response.append((news["title"], news["url"]))
    return response


# Requisito 11
def top_5_categories():
    db_news = find_news()
    cat_list = []
    for news in db_news:
        cat_list_news = news["categories"]
        for category in cat_list_news:
            cat_list.append(category)
    cat_list = Counter(cat_list)
    ordered_top_list = []
    for chave in cat_list.keys():
        ordered_top_list.append(chave)
    print(ordered_top_list)
    return sorted(ordered_top_list)[:5]
