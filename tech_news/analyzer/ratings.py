from tech_news.database import find_news
from tech_news.analyzer.search_engine import format_result
from operator import itemgetter


# Requisito 10
def top_5_news():
    news_list = find_news()
    top_news = [(
        (doc),
        doc["comments_count"] + doc["shares_count"]) for doc in news_list]
    news_sorted = (
        sorted(top_news, key=itemgetter(1), reverse=True))
    select_top_5_news = news_sorted[:5]
    my_list = [list_item[0] for list_item in select_top_5_news]
    return format_result(my_list)

# Sobre método sorted() e uso do operator.itemgetter:
# https://docs.python.org/pt-br/3/howto/sorting.html
# https://www.ti-enxame.com/pt/python/como-o-operator.itemgetter-e-sort-funcionam-em-python/1042252678/


def get_categories(key, news_list):
    categories_news_list = []
    for news in news_list:
        for each_category in news[key]:
            categories_news_list.append(each_category)
    return categories_news_list


def count_categories(categories_list):
    key = 0
    categories_ocurrences_count = []
    categories_final = []
    while key < len(categories_list):
        ocurrences = categories_list.count(categories_list[key])
        categories_ocurrences_count.append({categories_list[key]: ocurrences})
        for item in categories_ocurrences_count[key].items():
            categories_final.append(item)
            # Alternativa (lógica para eliminar repetição):
            # if item not in categories_final:
            #     categories_final.append(item)
        key += 1
    # Uso do set para eliminar repetições de tuplas
    return set(categories_final)
# Source:
# Como eliminar repetições de listas no Python:
# https://tutorial.eyehunts.com/python/python-remove-duplicates-from-dictionary-example-code/


# Requisito 11
def top_5_categories():
    news_list = find_news()
    categories_list = get_categories("categories", news_list)
    categories_list_count = count_categories(categories_list)
    categories_list_count_sorted = sorted(
        categories_list_count, key=itemgetter(0))
    select_top_5_categories = categories_list_count_sorted[:5]
    return [doc[0] for doc in select_top_5_categories]
