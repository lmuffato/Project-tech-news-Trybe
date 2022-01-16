from tech_news.database import find_news
import re
import datetime


# Requisito 6
def search_by_title(title):
    news_list = find_news()
    filtered_news_list = []
    for news in news_list:
        if re.search(news['title'], title, re.IGNORECASE):
            filtered_news_list.append((news['title'], news['url']))
    print(filtered_news_list)
    return filtered_news_list


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Data inválida')
    news_list = find_news()
    filtered_news_list = []
    for news in news_list:
        formated_date = news['timestamp'][0:10]
        if (formated_date == date):
            filtered_news_list.append((news['title'], news['url']))
    print(filtered_news_list)
    return filtered_news_list


# Requisito 8
def search_by_source(source):
    news_list = find_news()
    filtered_news_list = []
    for news in news_list:
        for s in news['sources']:
            if re.search(s, source, re.IGNORECASE):
                filtered_news_list.append((news['title'], news['url']))
    print(filtered_news_list)
    return filtered_news_list


# Requisito 9
def search_by_category(category):
    news_list = find_news()
    filtered_news_list = []
    for news in news_list:
        for c in news['categories']:
            if re.search(c, category, re.IGNORECASE):
                filtered_news_list.append((news['title'], news['url']))
    print(filtered_news_list)
    return filtered_news_list
