import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_source,
    search_by_category,
    search_by_date,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def menu():
    select = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )

    return select


def select_option_zero_to_two(option):
    if option == "0":
        aux = int(input("Digite quantas notícias serão buscadas:"))
        return get_tech_news(aux)
    if option == "1":
        aux = input("Digite o título:")
        return search_by_title(aux)
    if option == "2":
        aux = input("Digite a data no formato aaaa-mm-dd:")
        return search_by_date(aux)


def select_option_three_to_five(option):
    if option == "3":
        aux = input("Digite a fonte:")
        return search_by_source(aux)
    if option == "4":
        aux = input("Digite a categoria:")
        return search_by_category(aux)
    if option == "5":
        return top_5_news()


def select_option_six_and_seven(option):
    if option == "6":
        return top_5_categories()
    if option == "7":
        return print("Encerrando script")
    else:
        return sys.stderr.write("Opção inválida\n")


# Requisito 12
def analyzer_menu():
    selected = menu()

    if selected == "0" or selected == "1" or selected == "2":
        select_option_zero_to_two(selected)
    elif (
        selected == "3"
        or selected == "4"
        or selected == "5"
        or selected == "6"
    ):
        select_option_three_to_five(selected)
    else:
        select_option_six_and_seven(selected)
