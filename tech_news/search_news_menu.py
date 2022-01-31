import sys
from tech_news.analyzer.search_engine import (
    search_by_source,
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def search_news_functions(option):
    if option == 0:
        amount = input("Digite quantas notícias serão buscadas: ")
        if amount.isdigit():
            amount_validated = int(amount)
            return get_tech_news(amount_validated)
        else:
            print("Opção inválida\n", file=sys.stderr)
    elif option == 1:
        title = str(input("Digite o título: "))
        return search_by_title(title)
    elif option == 2:
        date = str(input("Digite a data no formato aaaa-mm-dd: "))
        return search_by_date(date)


def search_top_news(option):
    if option == 3:
        source = str(input("Digite a fonte :"))
        return search_by_source(source)
    elif option == 4:
        category = str(input("Digite a categoria: "))
        return search_by_category(category)
    elif option == 5:
        return top_5_news()
    elif option == 6:
        return top_5_categories()
