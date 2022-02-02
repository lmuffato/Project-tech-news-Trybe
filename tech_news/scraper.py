from parsel import Selector
import requests
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:  # Tenta realizar a ação
        # timeout é o limite em segundos para lançar o erro timeOut
        response = requests.get(url, timeout=3)
        time.sleep(1)  # espera 1 segundo para cada resquisição
        if response.status_code != 200:
            return None  # Se não retornar status 200, retorna nenhum valor
        return response.text  # Todo o html da página
    except requests.Timeout:  # Tratamento do erro Timeout
        return None  # no caso de erro de timeOut, retorna nenhum valor


# Teste manual
# print(fetch("https://www.tecmundo.com.br/novidades"))


# Requisito 2
def scrape_novidades(html_content):
    # "elementoPai.classe elementoFilho.class::attr(nomeAtributo)"
    css_selector = "h3.tec--card__title a.tec--card__title__link::attr(href)"
    # O seletor acima corresponde ao endereço do link desejado abaixo
    # <h3 class="tec--card__title">
    #   <a
    #     class="tec--card__title__link"
    #     href="link desejado"
    #    >
    #   </a>
    # </h3>
    # Acessando o valor do atribudo da tag html -> class::attr(nomeDoAtributo)"
    html_page = Selector(text=html_content)  # carrega a pagina html
    array_links = html_page.css(css_selector).getall()
    # Usa o seletor de css para retornar um array com as tags encontradas
    # .getll() retonra todas as ocorrências encontradas
    # retorna um array com os links de todas as notícias
    return array_links


# Teste manual
print(scrape_novidades(fetch("https://www.tecmundo.com.br/novidades")))


# Requisito 3
def scrape_next_page_link(html_content):
    css_selector = "a.tec--btn--lg::attr(href)"  # endereço do botão next
    html_page = Selector(text=html_content)  # carrega a pagina html
    url_next_page = html_page.css(css_selector).get()
    # .get() retorna o primeiro elemento encontrado
    return url_next_page


# Teste manual
# print(scrape_next_page_link(fetch("https://www.tecmundo.com.br/novidades")))

def getArrayElements(selector, cssSelector):
    elements = []
    # Pra cada elemento econtrado
    for element in selector.css(cssSelector).getall():
        # Adicionar a adicionar o elemento no array
        elements.append(element.strip())
    return elements


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)  # Todo o html da página

    # link da página disponível no head do html
    url = selector.css("head link[rel=canonical]::attr(href)").get()

    # Titulo da noticia
    title = selector.css(".tec--article__header__title::text").get()

    # Data de publicacao
    news_timestamp = selector.css("#js-article-date::attr(datetime)").get()

    writer = selector.css(".z--font-bold *::text").get()

    if writer:  # se o autor existir
        writer = writer.strip()  # retira possiveis espaços entre o nome
    else:
        writer = None

    # Quantidade de compartilhametos
    shares_count = selector.css(".tec--toolbar__item::text").get()

    # Tratamento do dados - removendo a string "Compartilharam"    
    if shares_count:
        # divide a string em duas e recupera a primeira (numero)
        shares_count = (shares_count.strip().split(" ")[0])
    else:
        shares_count = 0

    # Numero de comentarios
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()

    if comments_count is None:  # Se não tiver retorno
        comments_count = 0

    # Primeiro parágrafo
    summary_css = selector.css(
        # primeiro parágrafo dos elementos filhos abaixo do body
        ".tec--article__body > p:nth-child(1) *::text"
    ).getall()

    first_paragraph = "".join(summary_css)

    # Fontes
    sources = getArrayElements(selector, ".z--mb-16 div a::text")

    # Categorias
    categories = getArrayElements(selector, "#js-categories a::text")

    return {
        "url": url,
        "title": str(title),
        "timestamp": news_timestamp,
        "writer": str(writer),
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": str(first_paragraph),
        "sources": sources,
        "categories": categories,
    }


# Teste manual
# print(scrape_noticia(fetch("https://www.tecmundo.com.br/novidades")))


# Requisito 5
def get_tech_news(amount):
    # array qye recebe as informações de cada página
    news_links_list = []
    # Página html já formatada
    html_page = fetch("https://www.tecmundo.com.br/novidades")

    # Une elementos em um único array
    news_links_list.extend(scrape_novidades(html_page))

    # enquanto o numero de links não for menor que amount
    while len(news_links_list) <= amount:
        # recuper ao link da próxima página
        next_page_link = scrape_next_page_link(html_page)
        # recupara o html formatado
        next_page = fetch(next_page_link)
        # recupera todos os links de noticias e une ao array
        news_links_list.extend(scrape_novidades(next_page))

    # array com todos os objetos de todas as noticias
    all_news_info = []

    # para cada link em news_links_list
    for link in news_links_list[:amount]:
        # o parâmetro amount em news_links_list[:amount]
        # limita os elementos a serem iterados pelo for

        # faça uma requisão na página e recupere o html
        page = fetch(link)

        # salve todos os dados na noticia em um objeto
        # e acrescente esse objeto a um array
        all_news_info.append(scrape_noticia(page))

    # Salva o array no banco de dados através insert_many
    create_news(all_news_info)
    return all_news_info

# Teste manual
# print(get_tech_news(5))

# Obs: É necessário ligar o serviço do mongodb
# no terminal: sudo service mongod start

# conferir as informações salvas no mongodb
# no terminal: mongosh
# use tech_news
# db.news.find()
