from tech_news.database import find_news


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
    """Seu código deve vir aqui"""
