import sys
from scraper import get_tech_news
from analyzer.search_engine import (
    search_by_source, search_by_title, search_by_date, search_by_category)
from analyzer.ratings import top_5_categories, top_5_news


# Requisito 12
def analyzer_menu():

    option = input('Selecione uma das opções a seguir:\n'
                   ' 0 - Popular o banco com notícias;\n'
                   ' 1 - Buscar notícias por título;\n'
                   ' 2 - Buscar notícias por data;\n'
                   ' 3 - Buscar notícias por fonte;\n'
                   ' 4 - Buscar notícias por categoria;\n'
                   ' 5 - Listar top 5 notícias;\n'
                   ' 6 - Listar top 5 categorias;\n'
                   ' 7 - Sair.')

    inputs = {'0': input_get_news,
              '1': input_get_title,
              '2': input_get_date,
              '3': input_get_source,
              '4': input_get_category,
              '5': input_get_top_news,
              '6': input_get_top_categories,
              '7': input_close_app}

    return inputs[option]()


def input_get_title():
    print_data(search_by_title, 'Digite o título:')


def input_get_date():
    print_data(search_by_date,
               'Digite quantas notícias serão buscadas:')


def input_get_source():
    print_data(search_by_source, 'Digite a fonte:')


def input_get_category():
    print_data(search_by_category, 'Digite a categoria:')


def input_get_top_news():
    print(top_5_news())


def input_get_top_categories():
    print(top_5_categories())


def input_close_app():
    print('Encerrando script')


def print_data(function, input_text):
    try:
        value = input(input_text)
        print(function(value))
    except ValueError as err:
        print(err, file=sys.stderr)


def input_get_news():
    try:
        qty = input("Digite quantas notícias serão buscadas:")
        print(get_tech_news(int(qty)))
    except ValueError as err:
        print(err, file=sys.stderr)


if(__name__ == '__main__'):
    analyzer_menu()