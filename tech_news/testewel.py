from database import find_news
from pprint import pprint
from collections import Counter


# Requisito 11
def top_5_categories():
    news_list = []
    response = find_news()
    if len(response) == 0:
        return response
    for item in response:
        for cat in item["categories"]:
            news_list.append(cat)
    duplicates = Counter(news_list)
    top_typle = duplicates.most_common()
    categories_list = []
    for category in top_typle:
        categories_list.append(category[0])
    categories_list.sort()
    top_5_list = categories_list[:5]
    return top_5_list


pprint(top_5_categories())
