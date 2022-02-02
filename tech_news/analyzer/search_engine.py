from tech_news.database import search_news
from datetime import datetime


def newShapeElement(news_list):
    formatted_news_list = []  # array com os elementos formatados

    for news in news_list:
        # seleciona apenas o titulo e a url
        formatted_new = (news["title"], news["url"])
        formatted_news_list.append(formatted_new)

    return formatted_news_list


# Requisito 6
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

    return newShapeElement(news_list)


# Teste manual
# print(search_by_title("Vamoscomtudo"))


# Requisito 7
def search_by_date(date):
    try:
        # data no formato yyyy-mm-dd
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    news_list = search_news(
      {
        "timestamp": {
          "$regex": date,
          "$options": "i"
        }
      })

    return newShapeElement(news_list)

# Teste manual
# print(ssearch_by_date("2020-11-11"))


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
