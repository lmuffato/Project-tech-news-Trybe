from tech_news.scraper import get_tech_news
from tech_news.analyzer import search_engine
from tech_news.analyzer.ratings import top_5_categories, top_5_news


def search_title():
    return search_engine.search_by_title(input("Digite o título:"))


def search_date():
    return search_engine.search_by_date(input("Digite o título:"))


def search_source():
    return search_engine.search_by_source(input("Digite a fonte:"))


def search_category():
    return search_engine.search_by_category(input("Digite a categoria:"))


def get_news():
    while True:
        try:
            amount = int(input("Digite quantas notícias serão buscadas:"))
            return get_tech_news(amount)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


def choose_options():
    return input(
        """ Selecione uma das opções a seguir:
            0 - Popular o banco com notícias;
            1 - Buscar notícias por título;
            2 - Buscar notícias por data;
            3 - Buscar notícias por fonte;
            4 - Buscar notícias por categoria;
            5 - Listar top 5 notícias;
            6 - Listar top 5 categorias;
            7 - Sair. """
    )


# Requisito 12
def analyzer_menu():
    main_info = choose_options()

    my_list = {
        "0": get_news,
        "1": search_title,
        "2": search_date,
        "3": search_source,
        "4": search_category,
        "5": top_5_news,
        "6": top_5_categories,
    }

    response = 0

    try:
        if main_info == "7":
            return
        response = my_list[main_info]()
    except KeyError:
        print("Opção inválida")

    return response


x = analyzer_menu()
print(x)
