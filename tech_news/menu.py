import sys


# Requisito 12
def analyzer_menu():
    selected_option = input(
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

    options = {
        '0': 'Digite quantas notícias serão buscadas:',
        '1': 'Digite o título:',
        '2': 'Digite a data no formato aaaa-mm-dd:',
        '3': 'Digite a fonte:',
        '4': 'Digite a categoria:',
        '5': '',
        '6': '',
        '7': '',
    }

    try:
        if (selected_option in ['5', '6', '7']):
            pass
        else:
            input(options[selected_option])

    except KeyError:
        return print('Opção inválida', file=sys.stderr)
