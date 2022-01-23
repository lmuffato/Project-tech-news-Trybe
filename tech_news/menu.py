import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


# Requisito 12
OPTIONS = "\n ".join(
    [
        "Selecione uma das opções a seguir:",
        "0 - Popular o banco com notícias;",
        "1 - Buscar notícias por título;",
        "2 - Buscar notícias por data;",
        "3 - Buscar notícias por fonte;",
        "4 - Buscar notícias por categoria;",
        "5 - Listar top 5 notícias;",
        "6 - Listar top 5 categorias;",
        "7 - Sair.\n",
    ]
)


def zero():
    amount_of_news = int(input("Digite quantas notícias serão buscadas:"))

    return get_tech_news(amount_of_news)


def one():
    title = input("Digite o título:")

    return search_by_title(title)


def two():
    date = input("Digite a data no formato aaaa-mm-dd:")

    return search_by_date(date)


def three():
    source = input("Digite a fonte:")

    return search_by_source(source)


def four():
    category = input("Digite a categoria:")

    return search_by_category(category)


def seven():
    print("Encerrando script\n")


FUNCTIONS = {
    "0": zero,
    "1": one,
    "2": two,
    "3": three,
    "4": four,
    "5": lambda: top_5_news(),
    "6": lambda: top_5_categories(),
    "7": seven,
}


def analyzer_menu():
    selected_option = input(OPTIONS)

    try:
        print(FUNCTIONS[selected_option]())
    except KeyError:
        sys.stderr.write("Opção inválida\n")
