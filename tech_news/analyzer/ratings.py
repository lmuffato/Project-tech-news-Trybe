from operator import itemgetter
from tech_news.database import find_news
# from operator import itemgetter


def slice_5(items):
    return items[0:5]


# itemgetter Source:
# https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-itemgetter/
def top_5_news():
    news = find_news()
    popularity = sorted([
            {
                'title': new['title'],
                'url': new['url'],
                'popularity': new['comments_count'] + new['shares_count']
            }
            for new in news
        ], key=itemgetter('popularity'), reverse=True)
    top_5 = slice_5(popularity)
    return [tuple((new['title'], new['url'])) for new in top_5]


# Requisito 11
def top_5_categories():
    news = find_news()
    categories = sorted([
            category for new in news
            for category in new['categories']
        ])
    return slice_5(categories)
