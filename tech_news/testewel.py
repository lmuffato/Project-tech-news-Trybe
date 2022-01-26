from database import search_news


# Requisito 6
def search_by_title(title):
    if title == "":
        return []
    news_list = []
    response = search_news({"title": title.capitalize()})
    if len(response) == 0:
        return response
    for item in response:
        news_typle = item["title"], item["url"]
        news_list.append(news_typle)
    return news_list


search_title = "o futuro do trabalho será mesmo remoto?"
print(search_by_title(search_title))
