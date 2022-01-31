import sys
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_source,
    search_by_title,
    search_by_date,
)


# Requisito 12
def analyzer_menu():
    user_choice = input(
        "Selecione uma das opções a seguir:"
        "0 - Popular o banco com notícias;"
        "1 - Buscar notícias por título;"
        "2 - Buscar notícias por data;"
        "3 - Buscar notícias por fonte;"
        "4 - Buscar notícias por categoria;"
        "5 - Listar top 5 notícias;"
        "6 - Listar top 5 categorias;"
        "7 - Sair."
    )
    actions = {
            "0": lambda: get_tech_news(
                input("Digite quantas notícias serão buscadas:")
            ),
            "1": lambda: search_by_title(input("Digite o título:")),
            "2": lambda: search_by_date(
                input("Digite a data no formato aaaa-mm-dd:")
            ),
            "3": lambda: search_by_source(input("Digite a fonte:")),
            "4": lambda: search_by_category(input("Digite a categoria:")),
            "5": lambda: top_5_news(),
            "6": lambda: top_5_categories(),
            "7": lambda: print("Encerrando script"),
        }
    try:
        print(actions[user_choice]())
    except KeyError:
        sys.stderr.write("Opção inválida\n")
