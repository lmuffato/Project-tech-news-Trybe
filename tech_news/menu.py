import sys


# Requisito 12
def analyzer_menu():
    menu_options = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )

    response_message = {
        "0": "Digite quantas notícias serão buscadas:",
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a fonte:",
        "4": "Digite a categoria:",
        "5": "top_5_news",
        "6": "top_5_categories",
        "7": "Encerrando script",
    }

    try:
        print(response_message[menu_options])
    except KeyError:
        sys.stderr.write("Opção inválida\n")
