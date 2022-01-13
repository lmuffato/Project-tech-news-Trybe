from .scraper import get_tech_news
import sys
from .analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
    search_by_source
)
from .analyzer.ratings import (
    top_5_news,
    top_5_categories
)


# Requisito 12
def analyzer_menu():
    print(
        'Selecione uma das opções a seguir:\n '
        '0 - Popular o banco com notícias;\n '
        '1 - Buscar notícias por título;\n '
        '2 - Buscar notícias por data;\n '
        '3 - Buscar notícias por fonte;\n '
        '4 - Buscar notícias por categoria;\n '
        '5 - Listar top 5 notícias;\n '
        '6 - Listar top 5 categorias;\n '
        '7 - Sair.'
    )
    menu_option_mapping = {
        0: 'Digite quantas noticiais serão buscadas:',
        1: 'Digite o título:',
        2: 'Digite a data no formato aaaa-mm-dd:',
        3: 'Digite a fonte:',
        4: 'Digite a categoria:',
    }

    menu_action_mapping = {
        0: get_tech_news,
        1: search_by_title,
        2: search_by_date,
        3: search_by_source,
        4: search_by_category,
        5: top_5_news(),
        6: top_5_categories()
    }

    user_choice = input()
    try:
        if type(user_choice) != int:
            print('Opção inválida', file=sys.stderr)
        if int(user_choice) in menu_option_mapping.keys():
            print(menu_option_mapping[int(user_choice)])
            func_param = input()
            if int(user_choice) == 0:
                menu_action_mapping[int(user_choice)](func_param)
            else:
                print(menu_action_mapping[int(user_choice)](func_param))
        elif int(user_choice) in [5, 6]:
            print(menu_action_mapping[int(user_choice)])
        elif int(user_choice) == 7:
            print('Encerrando script')
    except (ValueError, IndexError) as err:
        print(err, file=sys.stderr)
