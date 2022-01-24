from tech_news.database import find_news
from tech_news.analyzer.search_engine import mount_tuple


def sort_filter(e):
    return e["total"]


def sum_comments_and_shares(list):
    sum_list = []
    for item in list:
        aux = item["shares_count"] + item["comments_count"]
        sum_list.append(
            {"title": item["title"], "url": item["url"], "total": aux}
        )

    sum_list.sort(reverse=True, key=sort_filter)

    return sum_list


# Requisito 10
def top_5_news():
    all_news = find_news()
    sum_list = sum_comments_and_shares(all_news)

    final_list = [(item["title"], item["url"]) for item in sum_list[:5]]

    return final_list


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
