from tech_news.database import search_news


# Requisito 6
# {"title": {"$regex": "Vamoscomtudo", "$options": "i"}}

def search_by_title(title):
    news_list = search_news(
      {
        "title": {
          "$regex": title,
          "$options": "i"  # "case insensitive
          }
      })
    # Equivale a:
    # db.news.find({"title": {"$regex": "Vamoscomtudo", "$options": "i"}})

    formatted_news_list = []

    for news in news_list:
        # seleciona apenas o titulo e a url
        formatted_new = (news["title"], news["url"])
        formatted_news_list.append(formatted_new)

    return formatted_news_list


# Teste manual
# print(search_by_title("Vamoscomtudo"))


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
