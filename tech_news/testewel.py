from pprint import pprint
from tech_news.search_news_menu import search_news
from tech_news.search_news_menu import search_top_news


# Requisito 12
def analyzer_menu():
    option = ""
    print("Selecione uma das opções a seguir:\n")
    print(
        "0 - Popular o banco com notícias;\n1 - Buscar notícias por título;"
        + "\n2 - Buscar notícias por data;\n3 - Buscar notícias por fonte;"
        + "\n4 - Buscar notícias por categoria;\n5 - Listar top 5 notícias;"
        + "\n6 - Listar top 5 categorias;\n7 - Sair."
    )

    def isnumber(option):
        if option < 0 or option > 7:
            option = int(input("Escolha um número entre 0-7: "))
            isnumber(option)

    option = int(input("Escolha um número entre 0-7: "))
    isnumber(option)

    if option >= 0 and option < 4:
        return search_news(option)
    elif option >= 4 and option < 7:
        return search_top_news(option)
    else:
        return "Volte sempre meu parceiro"


pprint(analyzer_menu())
