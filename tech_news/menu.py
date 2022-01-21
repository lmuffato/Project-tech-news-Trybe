import sys

from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_source
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.ratings import top_5_news
from tech_news.analyzer.ratings import top_5_categories


# Requisito 12
# option 0
def get_tech_news_option():
    amt = input('Digite quantas notícias serão buscadas:')
    news = get_tech_news(int(amt))

    for n in news:
        print(n)


# option 1
def search_by_title_option():
    title = input('Digite o título:')
    news_by_title = search_by_title(title)

    for n in news_by_title:
        print(n)


# option 2
def search_by_date_option():
    date = input('Digite a data no formato aaaa-mm-dd:')
    news_by_date = search_by_date(date)

    print(news_by_date)


# option 3
def search_by_source_option():
    source = input('Digite a fonte:')
    news_by_source = search_by_source(source)

    print(news_by_source)


# option 4
def search_by_category_option():
    category = input('Digite a categoria:')
    news_by_category = search_by_category(category)

    print(news_by_category)


# option 5
def top_5_news_option():
    top_5 = top_5_news()
    print(top_5)


# option 6
def top_5_categories_option():
    top_5_cat = top_5_categories()
    print(top_5_cat)


# option 7
def exit_option():
    print('Encerrando script')
    return None


def analyzer_menu():
    option = input(
        'Selecione uma das opções a seguir:\n'
        ' 0 - Popular o banco com notícias;\n'
        ' 1 - Buscar notícias por título;\n'
        ' 2 - Buscar notícias por data;\n'
        ' 3 - Buscar notícias por fonte;\n'
        ' 4 - Buscar notícias por categoria;\n'
        ' 5 - Listar top 5 notícias;\n'
        ' 6 - Listar top 5 categorias;\n'
        ' 7 - Sair.\n'
    )

    menu_selection = {
        '0': get_tech_news_option,
        '1': search_by_title_option,
        '2': search_by_date_option,
        '3': search_by_source_option,
        '4': search_by_category_option,
        '5': top_5_news_option,
        '6': top_5_categories_option,
        '7': exit_option,
    }

    try:
        menu_selection[option]()
    except KeyError:
        sys.stderr.write('Opção inválida\n')
