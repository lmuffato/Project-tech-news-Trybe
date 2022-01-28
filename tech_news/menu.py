# Requisito 12
def analyzer_menu():
    enun = 'Selecione uma das opções a seguir:\n'
    op0 = '0 - Popular o banco com notícias;\n'
    op1 = '1 - Buscar notícias por título;\n'
    op2 = '2 - Buscar notícias por data;\n'
    op3 = '3 - Buscar notícias por fonte;\n'
    op4 = '4 - Buscar notícias por categoria;\n'
    op5 = '5 - Listar top 5 notícias;\n'
    op6 = '6 - Listar top 5 categorias;\n'
    op7 = '7 - Sair.\n'
    print(enun + op0 + op1 + op2 + op3 + op4 + op5 + op6 + op7)
    option = input()
    if option == '0':
        print("Digite quantas notícias serão buscadas:")
    if option == '1':
        print("Digite o título:")
    if option == '2':
        print("Digite a data no formato aaaa-mm-dd:")
    if option == '3':
        print("Digite a fonte:")
    if option == '4':
        print("Digite a categoria:")
    else:
        raise ValueError("Opção inválida")
