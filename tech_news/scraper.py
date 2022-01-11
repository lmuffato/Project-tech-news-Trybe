import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None

# print(fetch("http://quotes.toscrape.com/page/1"))


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links_list = []
    for news_link in selector.css("h3.tec--card__title"):
        link = news_link.css("a.tec--card__title__link::attr(href)").get()
        links_list.append(link)
    return links_list


# Documentação Parsel:
# https://parsel.readthedocs.io/en/latest/usage.html


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css("a.tec--btn::attr(href)").get()
    if next_page_link:
        return next_page_link
    else:
        return None


def format_strings(str_list):
    key = 0
    list_formatted = []
    while key < len(str_list):
        list_item = str_list[key].strip()
        list_formatted.append(list_item)
        key += 1
    return list_formatted


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news_dict = {
        "url": "",
        "title": "",
        "timestamp": "",
        "writer": "",
        "shares_count": 0,
        "comments_count": 0,
        "summary": "",
        "sources": [],
        "categories": []
    }
    for news in selector.xpath('//html[contains(@lang, "pt-BR")]'):
        noticia_url = news.xpath('//meta[contains(@property, "url")]')
        news_url = noticia_url.xpath('@content').get()
        title = news.css('h1.tec--article__header__title::text').get()
        writer = news.css('a.tec--author__info__link::text').get().strip()
        full_text = news.css('div.tec--article__body').xpath('./p')
        summary = full_text.get()
        categories = news.xpath('//div[contains(@id, "js-categories")]')
        categories_list = format_strings(
            categories.xpath('./a/text()').getall())
        sources = news.css('div.z--mb-16').xpath('./a//text()').getall()

        news_dict["url"] = news_url
        news_dict["title"] = title
        news_dict["writer"] = writer
        news_dict["summary"] = summary
        news_dict["categories"] = categories_list
        news_dict["sources"] = sources

    return news_dict


test = fetch(
    "https://www.tecmundo.com.br/produto/231765-buser-vale-pena-conheca-servico-viagens-onibus.htm"
)
print(scrape_noticia(test))
# Source:
# Sobre strip():
# https://dev.to/jacob777baltimore/python-remove-all-whitespace-4m3n


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
