from tech_news.database import find_news
import operator


# Requisito 10
def top_5_news():
    news = find_news()
    top_news = [(
        (item["title"], item["url"]),
        int(item["comments_count"]) + int(item["shares_count"])
    ) for item in news]

    top_news.sort(key=lambda x: x[1], reverse=True)
    cut_top_news = top_news[:5]

    my_list = [item[0] for item in cut_top_news]

    return my_list


# print(top_5_news())

def get_category():
    news = find_news()
    item = []

    for new in news:
        for category in new["categories"]:
            item.append(category)

    return item


def get_ocorrencies(item):
    aux = {}

    for i in range(len(item)):
        if not item[i] in aux:
            aux[item[i]] = 1
        else:
            continue
        for j in range(i + 1, len(item)):
            if item[i] == item[j]:
                aux[item[i]] += 1

    return aux


# Requisito 11
def top_5_categories():
    item = get_category()
    aux = get_ocorrencies(item)

    sorted_tuples = sorted(
        aux.items(), key=operator.itemgetter(0)
    )

    my_list = []

    for k in sorted_tuples:
        my_list.append(k[0])

    list = my_list[:5]

    final_list = sorted(list)

    return final_list


print(top_5_categories())
