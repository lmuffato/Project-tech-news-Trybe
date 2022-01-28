import sys


# Requisito 12
def answer_menu(answer):
    if answer == '0':
        print("Digite quantas notícias serão buscadas:")
    if answer == '1':
        print("Digite o título:")
    elif answer == '2':
        print("Digite a data no formato aaaa-mm-dd:")
    elif answer == '3':
        print("Digite a fonte:")
    elif answer == '4':
        print("Digite a categoria:")
    else:
        sys.stderr.write("Opção inválida\n")


def analyzer_menu():
    menu = (
            'Selecione uma das opções a seguir:\n' +
            ' 0 - Popular o banco com notícias;\n' +
            ' 1 - Buscar notícias por título;\n' +
            ' 2 - Buscar notícias por data;\n' +
            ' 3 - Buscar notícias por fonte;\n' +
            ' 4 - Buscar notícias por categoria;\n' +
            ' 5 - Listar top 5 notícias;\n' +
            ' 6 - Listar top 5 categorias;\n' +
            ' 7 - Sair.'
    )
    option = input(menu)
    answer_menu(option)



# analyzer_menu()
