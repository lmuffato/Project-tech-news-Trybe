from tech_news.database import find_news


def sum_comments_and_shares(list):
    sum_list = []

    for item in list:
        aux = item["shares_count"] + item["comments_count"]
        sum_list.append({"index": list.index(item), "total": aux})

    return sum_list


# Requisito 10
def top_5_news():
    order_news = []
    counter = 0
    all_news = find_news()
    sum = sum_comments_and_shares(all_news)
    
    print(sum)
        


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
