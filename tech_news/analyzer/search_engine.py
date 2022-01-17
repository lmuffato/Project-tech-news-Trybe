from tech_news.database import search_news
import time


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
    try:
        # 1º verifica se a data é válida. Se for continua o código.
        time.strptime(date, "%Y-%m-%d")

        buscador = search_news({"timestamp": {"$regex": date}})

        lista_de_noticias = []
        for noticia in buscador:
            noticia_selecionada = (noticia["title"], noticia["url"])
            lista_de_noticias.append(noticia_selecionada)

        return lista_de_noticias

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    buscador = search_news({"sources": {"$regex": source, "$options": "i"}})

    lista_de_noticias = []
    for noticia in buscador:
        noticia_selecionada = (noticia["title"], noticia["url"])
        lista_de_noticias.append(noticia_selecionada)

    return lista_de_noticias


# Requisito 9
def search_by_category(category):
    busca = search_news({"categories": {"$regex": category, "$options": "i"}})

    lista_de_noticias = []
    for noticia in busca:
        noticia_selecionada = (noticia["title"], noticia["url"])
        lista_de_noticias.append(noticia_selecionada)

    return lista_de_noticias
