import sys


# Requisito 12
def analyzer_menu():
    info = input(
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

    options = {
        "0": lambda: input("Digite quantas notícias serão buscadas:"),
        "1": lambda: input("Digite o título:"),
        "2": lambda: input("Digite a data no formato aaaa-mm-dd:"),
        "3": lambda: input("Digite a fonte:"),
        "4": lambda: input("Digite a categoria:"),
    }

    try:
        print(options[info]())
    except KeyError:
        sys.stderr.write("Opção inválida\n")
