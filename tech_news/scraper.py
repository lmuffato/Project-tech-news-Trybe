import time
import requests
import parsel
from .database import create_news


# Requisito 1 - Pega o conteúdo do site
def fetch(url):
    try:
        # README: "utilizar time.sleep(1) antes de cada requisição"
        time.sleep(1)
        requisicao = requests.get(url, timeout=3)

        if requisicao.status_code == 200:
            return requisicao.text
        else:
            return None

    except requests.Timeout:
        return None


# Requisito 2 - Separa os links de notícias
def scrape_novidades(html_content):
    conteudo = parsel.Selector(html_content)
    links = []

    for link in conteudo.css("h3.tec--card__title"):
        noticia = link.css("a.tec--card__title__link::attr(href)").get()
        links.append(noticia)

    return links


# Requisito 3 - Verifica se tem botão para próxima página
def scrape_next_page_link(html_content):
    conteudo = parsel.Selector(html_content)
    botao = conteudo.css("a.tec--btn::attr(href)").get()

    if botao:
        return botao
    else:
        return None


# Requisito 4 - Pega os detalhes da notícia
# Gabriel Pereira, Eduardo Costa, Tiago Santos e EU estudamos
# juntos o requisito 4 na Room 2 do plantão do dia 12/01/2022


def qual_seletor(conteudo):
    # Para resolver o erro do avaliador local nesta função "qual_seletor",
    # recebi ajuda dos alunos: Renan Oliveira, Rafael Medeiros, Fernando
    # Resende e do instrutor Carlos Melo. O site do Tecmundo utiliza mais
    # de uma classe ao informar o nome do autor (13/01/2022)
    classe_01 = conteudo.css(".tec--timestamp__item a::text").get()
    classe_02 = conteudo.css("a.tec--author__info__link::text").get()
    classe_03 = conteudo.css(".tec--author__info > p:first-child::text").get()

    if classe_01 is not None:
        autor = classe_01.strip()
        return autor
    elif classe_02 is not None:
        autor = classe_02.strip()
        return autor
    elif classe_03 is not None:
        autor = classe_03.strip()
        return autor
    else:
        return None


def fontes_da_noticia(conteudo):
    lista_de_fontes = []
    buscar_fontes = conteudo.css("div.z--mb-16 a::text").getall()

    for fonte in buscar_fontes:
        lista_de_fontes.append(fonte.strip())
        # https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_strip
        # .strip() serve para tirar os espaços no início e no final
        # Exemplo: " Venture Beat " > "Venture Beat"

    return lista_de_fontes


def lista_de_categorias(conteudo):
    categorias = []
    buscar_categorias = conteudo.css("div#js-categories a::text").getall()

    for categoria in buscar_categorias:
        categorias.append(categoria.strip())

    return categorias


def scrape_noticia(html_content):
    conteudo = parsel.Selector(html_content)
    noticia = {}
    url = conteudo.css("head link[rel=canonical]::attr(href)").get()
    titulo = conteudo.css("h1.tec--article__header__title::text").get()
    data = conteudo.css("time#js-article-date::attr(datetime)").get()
    autor = qual_seletor(conteudo)

    # Regex aprendido com a instrução durante o plantão
    envios = conteudo.css("div.tec--toolbar__item::text").re_first(r"\d+")
    compartilhamentos = int(envios) if envios else 0

    comentarios = int(conteudo.css("button.tec--btn::attr(data-count)").get())
    sumario = "".join(
        # Precisou usar o ">" da linha abaixo para passar no requisito 5
        # Ele faz parar exatamente no conteúdo da <p> ... </p>
        conteudo.css("div.tec--article__body > p:first-child *::text").getall()
    )
    fontes = fontes_da_noticia(conteudo)
    categorias = lista_de_categorias(conteudo)

    noticia.update(url=url, title=titulo, timestamp=data, writer=autor)
    noticia.update(shares_count=compartilhamentos, comments_count=comentarios)
    noticia.update(summary=sumario, sources=fontes, categories=categorias)

    return noticia


# Executar "python3 scraper.py" dentro da pasta "tech_news"
# Descomentar abaixo para testar manualmente o requisito 4
# a = fetch("https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/
# 155000-musk-tesla-carros-totalmente-autonomos.htm")
# print(scrape_noticia(a))


# Requisito 5 - Separa a quantidade de notícias desejadas
def get_tech_news(amount):
    # Usa o site do Tecmundo como referência
    URL_noticias = fetch("https://www.tecmundo.com.br/novidades")

    # Separa os links das noticias da 1ª página
    links_noticias = scrape_novidades(URL_noticias)

    # Verifica se a quantidade de notícias desejadas pode ser encontrada
    # apenas na 1ª página. Se a quantidade for insuficiente, vai pegar
    # notícias das próximas páginas e juntar com as notícias da 1ª página.
    while len(links_noticias) < amount:
        proxima_pagina = scrape_next_page_link(URL_noticias)
        noticias_proxima_pagina = fetch(proxima_pagina)
        links_noticias.extend(scrape_novidades(noticias_proxima_pagina))

    noticias = []

    for link in links_noticias[:amount]:
        novo_conteudo = fetch(link)
        nova_noticia = scrape_noticia(novo_conteudo)
        noticias.append(nova_noticia)

    create_news(noticias)

    return noticias
