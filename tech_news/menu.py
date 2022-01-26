import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def case_zero():
    user_choice = int(input("Digite quantas notícias serão buscadas:\n"))
    try:
        result = get_tech_news(user_choice)
        return result
    except Exception as err:
        return print(f"Deu ruim, toma: {err}", file=sys.stderr)


def case_one():
    user_choice = input("Digite o título:\n")
    try:
        result = search_by_title(user_choice)
        return result
    except Exception as err:
        return print(f"Deu ruim, toma: {err}", file=sys.stderr)


def case_two():
    user_choice = input("Digite a data no formato aaaa-mm-dd:\n")
    try:
        result = search_by_date(user_choice)
        return result
    except Exception as err:
        return print(f"Deu ruim, toma: {err}", file=sys.stderr)


def case_three():
    user_choice = input("Digite a fonte:\n")
    try:
        result = search_by_source(user_choice)
        return result
    except Exception as err:
        return print(f"Deu ruim, toma: {err}", file=sys.stderr)


def case_four():
    user_choice = input("Digite a categoria:\n")
    try:
        result = search_by_category(user_choice)
        return result
    except Exception as err:
        return print(f"Deu ruim, toma: {err}", file=sys.stderr)


def case_five():
    try:
        result = top_5_news()
        return result
    except Exception as err:
        return print(f"Deu ruim, toma: {err}", file=sys.stderr)


def case_six():
    try:
        result = top_5_categories()
        return result
    except Exception as err:
        return print(f"Deu ruim, toma: {err}", file=sys.stderr)


def case_seven():
    print("Encerrando script\n")
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
        "5": case_five,
        "6": case_six,
        "7": case_seven,
    }

    if chosen_option not in switch_options:
        return print("Opção inválida", file=sys.stderr)

    return switch_options[chosen_option]()
