import sys


def case_zero():
    input("Digite quantas notícias serão buscadas:\n")


def case_one():
    input("Digite o título:\n")


def case_two():
    input("Digite a data no formato aaaa-mm-dd:\n")


def case_three():
    input("Digite a fonte:\n")


def case_four():
    input("Digite a categoria:\n")


def case_seven():
    sys.stdin.close()


# Requisito 12
def analyzer_menu():
    chosen_option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )
    switch_options = {
         "0": case_zero,
         "1": case_one,
         "2": case_two,
         "3": case_three,
         "4": case_four,
         "7": case_seven,
    }

    if chosen_option not in switch_options:
        return print("Opção inválida", file=sys.stderr)

    return switch_options[chosen_option]()
