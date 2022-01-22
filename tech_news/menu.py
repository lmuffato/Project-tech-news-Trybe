import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


menu_labels = [
    {
        "input_label": "Popular o banco com notícias;",
        "input_message": "Digite quantas notícias serão buscadas:",
    },
    {
        "input_label": "Buscar notícias por título;",
        "input_message": "Digite o título:",
    },
    {
        "input_label": "Buscar notícias por data;",
        "input_message": "Digite a data no formato aaaa-mm-dd:",
    },
    {
        "input_label": "Buscar notícias por fonte;",
        "input_message": "Digite a fonte:",
    },
    {
        "input_label": "Buscar notícias por categoria;",
        "input_message": "Digite a categoria:",
    },
    {
        "input_label": "Listar top 5 notícias;",
        "input_message": "",
    },
    {
        "input_label": "Listar top 5 categorias;",
        "input_message": "",
    },
    {"input_label": "Sair.", "input_message": ""},
]


def take_input():
    sys.stdout.write("Selecione uma das opções a seguir:")
    sys.stdout.write(
        "".join(
            [
                f"\n {i} - {x['input_label']}"
                for x, i in zip(menu_labels, range(len(menu_labels)))
            ]
        )
        + "\n"
    )

    try:
        std_input = input()

        return (menu_labels[int(std_input)], int(std_input))
    except (KeyError, ValueError, IndexError, StopIteration):
        return (None, None)


def zero():
    n = input()
    print(get_tech_news(int(n)))


def um():
    title = input()
    print(search_by_title(title))


def dois():
    date = input()
    print(search_by_date(date))


def tres():
    source = input()
    print(search_by_source(source))


def quatro():
    category = input()
    print(search_by_category(category))


def cinco():
    print(top_5_news())


def seis():
    print(top_5_categories())


items = {
    0: zero,
    1: um,
    2: dois,
    3: tres,
    4: quatro,
    5: cinco,
    6: seis,
}


# Requisito 12
def analyzer_menu():
    while True:
        inp, index = take_input()

        if inp is None:
            sys.stderr.write("Opção inválida\n")
            break

        print(inp["input_message"])

        if index == 7:
            print("Encerrando script")
            break

        items[index]()


# analyzer_menu()
