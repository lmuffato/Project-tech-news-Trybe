from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:  # Tenta realizar a ação
        # timeout é o limite em segundos para lançar o erro timeOut
        response = requests.get(url, timeout=3)
        time.sleep(1)   # espera 1 segundo para cada resquisição
        if response.status_code != 200:
            return None   # Se não retornar status 200, retorna nenhum valor
        return response.text   # Todo o html da página
    except requests.Timeout:   # Tratamento do erro Timeout
        return None   # no caso de erro de timeOut, retorna nenhum valor


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
    return array_links


# Teste manual
# print(scrape_novidades(fetch("https://www.tecmundo.com.br/novidades")))


# Requisito 3
def scrape_next_page_link(html_content):
    css_selector = "a.tec--btn--lg::attr(href)"  # endereço do botão next
    html_page = Selector(text=html_content)  # carrega a pagina html
    url_next_page = html_page.css(css_selector).get()
    # .get() retorna o primeiro elemento encontrado
    return url_next_page


# Teste manual
# print(scrape_next_page_link(fetch("https://www.tecmundo.com.br/novidades")))


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
