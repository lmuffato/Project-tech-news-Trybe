import requests
import time
import parsel
from .database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    novidades = parsel.Selector(html_content)
    return novidades.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    conteudoHtml = parsel.Selector(html_content)
    url = conteudoHtml.css("a.tec--btn::attr(href)").get()
    if url:
        return url
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    tecmundo = parsel.Selector(html_content)
    url = tecmundo.css("head link[rel=canonical]::attr(href)").get()
    titulo = tecmundo.css("h1.tec--article__header__title::text").get()
    data_hora = tecmundo.css("time#js-article-date::attr(datetime)").get()
    autor_1 = tecmundo.css(".tec--author__info__link::text").get()
    autor_2 = tecmundo.css("div.tec--timestamp__item a::text").get()
    autor_3 = tecmundo.css("div.tec--author__info p.z--font-bold::text").get()

    if autor_1:
        autor = autor_1
    elif autor_2:
        autor = autor_2
    else:
        autor = autor_3

    compartilhamento = tecmundo.css(".tec--toolbar__item::text").get()
    comentarios = tecmundo.css("#js-comments-btn::attr(data-count)").get()
    resumo = "".join(tecmundo.css(
        ".tec--article__body > p:first-child *::text").getall())
    fonte = [item.strip() for item in tecmundo.css(
        "div.z--mb-16 div a::text"
        ).getall()]
    categoria = [item.strip() for item in tecmundo.css(
        "#js-categories a::text"
        ).getall()]

    return {
        "url": url,
        "title": titulo,
        "timestamp": data_hora,
        "writer": autor.strip() if autor else None,
        "shares_count": int(
            compartilhamento.split()[0]) if compartilhamento else 0,
        "comments_count": int(comentarios) if comentarios else 0,
        "summary": resumo,
        "sources": fonte,
        "categories": categoria,
    }


# Requisito 5
def get_tech_news(amount):
    Url = fetch("https://www.tecmundo.com.br/novidades")
    links = scrape_novidades(Url)
    while len(links) < amount:
        prox_pag = scrape_next_page_link(Url)
        not_prox_pag = fetch(prox_pag)
        links.extend(scrape_novidades(not_prox_pag))
    conteudo_novo = []
    for link in links[:amount]:
        conteudo = fetch(link)
        noticia_nova = scrape_noticia(conteudo)
        conteudo_novo.append(noticia_nova)

    create_news(conteudo_novo)
    return conteudo_novo
