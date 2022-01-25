from tech_news.scraper import get_tech_news
from tech_news.analyzer import search_engine, ratings


def menu():
    select = int(
        input(
            "Selecione uma das opções a seguir:\n"
            "0 - Popular o banco com notícias;\n"
            "1 - Buscar notícias por título;\n"
            "2 - Buscar notícias por fonte;\n"
            "4 - Buscar notícias por categoria;\n"
            "5 - Listar top 5 notícias;\n"
            "6 - Listar top 5 categorias;\n"
            "7 - Sair."
        )
    )

    return select


def select_option_zero_to_two(option):
    if option == 0:
        int(input("Digite quantas notícias serão buscadas:"))
        get_tech_news()
    if option == 1:
        aux = input("Digite o título:")
        search_engine.search_by_title(aux)
    if option == 2:
        aux = input("Digite a data no formato aaaa-mm-dd:")
        search_engine.search_by_date(aux)


def select_option_three_to_five(option):
    if option == 3:
        aux = input("Digite a fonte:")
        search_engine.search_by_source(aux)
    if option == 4:
        aux = input("Digite a categoria:")
        search_engine.search_by_category(aux)
    if option == 5:
        ratings.top_5_news()


def select_option_six_and_seven(option):
    if option == 6:
        ratings.top_5_categories()
    elif option == 7:
        print("Encerrando script")
    else:
        print("Opção inválida")


# Requisito 12
def analyzer_menu():
    selected = menu()
    if selected >= 0 or selected < 3:
        select_option_zero_to_two(selected)
    elif selected >= 3 or selected < 6:
        select_option_three_to_five(selected)
    else:
        select_option_six_and_seven(selected)
