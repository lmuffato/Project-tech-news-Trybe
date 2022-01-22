from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    # pesquisa sobre busca usando case sensitive
    # https://docs.mongodb.com/manual/reference/method/db.collection.find/
    # https://docs.mongodb.com/manual/reference/operator/query/regex/#mongodb-query-op.-regex

    results = search_news({"title": {"$regex": title, "$options": "i"}})
    response = []

    for result in results:
        title_search = result['title']
        url_search = result['url']

        response.append(title_search)
        response.append(url_search)

    if response:
        return [tuple(response)]
    else:
        return []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
