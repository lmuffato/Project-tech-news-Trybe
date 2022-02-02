from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    news_list = find_news()
    if news_list is None:
        return []

    news_list.sort(
        # A ordem padrão é decrescente
        reverse=True,  # para inverter a ordem padrão
        # o primeiro parâmetro para a ordem é o shares_count
        # o segundo parâmetro é 'comments_count'
        key=lambda new: new['shares_count'] + new['comments_count']
    )

    formatted_news_list = []

    for news in news_list[:5]:
        formatted_new = (news["title"], news["url"])
        formatted_news_list.append(formatted_new)

    return formatted_news_list


# Teste manual
# print(top_5_news())


# Requisito 11
def top_5_categories():
    news_list = find_news()
    categories = []

    if news_list is None:
        return []

    for new in news_list:

        # construi um array com todos os elementos do array categories
        categories.extend([*new['categories']])
    # Cria um dicionário composto pelo conjunto chave:valor
    # A chave é o elemento e valor é o numero de ocorrências no array
    occurrences = Counter(categories)

    # Cria a regra para ordenar de acordo com o valor da chave
    sorte_by_popularity = sorted(
        occurrences, key=occurrences.get, reverse=True
    )

    # Retorna o array organizado até os 5 primeiros elementos
    return sorted(sorte_by_popularity)[:5]


# Teste manual
# print(top_5_categories())


# A função acima poderia ter sido substituida pelo aggregate do mongodb
# fazendo a fitlragem e comparação pelo back-end

# db.news.aggregate(
#   [
#     { $unwind: "$categories" },
#     {
#       $group: {
#           "_id": {
#           "categorie": "$categories"
#         },
#         "total": { "$sum" : 1 }
#       }
#     },
#     { $sort : { total : -1 } },
#     { $limit : 5 },
#   ]
# );

# O operador $unwind "desconstrói" um campo array do documento de entrada e
# gera como saída um documento para cada elemento do array.
