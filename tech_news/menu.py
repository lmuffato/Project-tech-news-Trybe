import sys


# Requisito 12
def option(id, text, answer_input):
    if answer_input == id:
        print(text)
        return True
    return False


def answer_menu(answer_input):
    if (
        option("0", "Digite quantas notícias serão buscadas:", answer_input)
        or option("1", "Digite quantas notícias serão buscadas:", answer_input)
        or option("2", "Digite quantas notícias serão buscadas:", answer_input)
        or option("3", "Digite quantas notícias serão buscadas:", answer_input)
        or option("4", "Digite quantas notícias serão buscadas:", answer_input)
    ):
        pass
    else:
        sys.stderr.write("Opção inválida\n")


def analyzer_menu():
    menu = (
        "Selecione uma das opções a seguir:\n"
        + " 0 - Popular o banco com notícias;\n"
        + " 1 - Buscar notícias por título;\n"
        + " 2 - Buscar notícias por data;\n"
        + " 3 - Buscar notícias por fonte;\n"
        + " 4 - Buscar notícias por categoria;\n"
        + " 5 - Listar top 5 notícias;\n"
        + " 6 - Listar top 5 categorias;\n"
        + " 7 - Sair."
    )
    option = input(menu)
    answer_menu(option)
