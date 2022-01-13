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


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
