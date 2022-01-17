from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    # {"$regex": title, "$options": "i"} => Serve para indicar que a busca
    # pelo título não é Case Sensitive. Fonte de pesquisa abaixo:
    # https://docs.mongodb.com/manual/reference/operator/query/regex/
    buscador = search_news({"title": {"$regex": title, "$options": "i"}})

    lista_de_noticias = []
    for noticia in buscador:
        noticia_selecionada = (noticia["title"], noticia["url"])
        lista_de_noticias.append(noticia_selecionada)

    return lista_de_noticias


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
