import sys
from tech_news.search_news_menu import search_top_news, search_news_functions


# Requisito 12
def analyzer_menu():
    print(
        "Selecione uma das opções a seguir:\n "
        "0 - Popular o banco com notícias;\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por fonte;\n "
        "4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n "
        "6 - Listar top 5 categorias;\n "
        "7 - Sair."
    )

    option = input()

    if option.isdigit():
        option_validated = int(option)
        if option_validated >= 0 and option_validated < 3:
            return search_news_functions(option_validated)
        elif option_validated >= 3 and option_validated < 7:
            return search_top_news(option_validated)
        elif option_validated == 7:
            print("Encerrando script")
    else:
        print("Opção inválida\n", file=sys.stderr)
