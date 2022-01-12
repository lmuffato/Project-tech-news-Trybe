from .scraper import get_tech_news
from .analyzer.search_engine import search_by_title, search_by_date
from .analyzer.search_engine import search_by_source, search_by_category
from .analyzer.ratings import top_5_categories, top_5_news
import sys


def finish_script():
    print("Encerrando script")


# Requisito 12
def analyzer_menu():
    option = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""
    )

    options = {
        "0": get_tech_news,
        "1": search_by_title,
        "2": search_by_date,
        "3": search_by_source,
        "4": search_by_category,
        "5": top_5_news,
        "6": top_5_categories,
        "7": finish_script,
    }

    message = {
        "0": "Digite quantas notícias serão buscadas: ",
        "1": "Digite o título: ",
        "2": "Digite a data no formato aaaa-mm-dd: ",
        "3": "Digite a fonte: ",
        "4": "Digite a categoria: ",
    }

    if option not in options.keys():
        sys.stderr.write("Opção inválida\n")
        return

    if 0 <= int(option) <= 4:
        amount = input(message[option])
        return options[option](amount)

    return options[option]()
