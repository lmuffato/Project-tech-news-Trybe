import requests
import parsel
import time
import re
import json


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url=url, timeout=3)
        if response.ok:
            return response.text
        else:
            return None
    except requests.exceptions.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(text=html_content)
    res = selector.css(".tec--list .tec--card__title__link")
    return list(map(lambda x: x.attrib["href"], res))


# Requisito 3
def scrape_next_page_link(html_content):
    # try:
    #     url, pageNum = re.search(
    #         r"(\S+\/novidades\?page=)(\d+)", html_content
    #     ).groups()
    #     return f"{url}{int(pageNum)+1}"
    # except AttributeError:
    #     return "https://www.tecmundo.com.br/novidades?page=2"
    selector = parsel.Selector(text=html_content)
    return selector.css('.tec--list a.tec--btn::attr("href")').get()


# Requisito 4
def extract_count(strings_list, regex_r):
    output = 0
    for y in strings_list:
        try:
            regex = re.search(regex_r, y)
            return int(regex.groups()[0])
        except AttributeError:
            pass
    return output


def parse_json_writer(jsons_str):
    output = None
    for json_str in jsons_str:
        if json_str is None:
            return None

        try:
            deserialized_json = json.loads(json_str)
            output = deserialized_json["author"]["name"]
        except KeyError:
            pass

    return output


def extract_writer(selector):
    selectors = [
        selector.css(".tec--author__info__link::text").get(),
        selector.css(
            ".z--flex tec--timestamp tec--timestamp__item::text"
        ).get(),
        parse_json_writer(
            selector.css('script[type="application/ld+json"]::text').getall()
        ),
    ]

    for writer in selectors:
        if writer is not None:
            return str.strip(writer)

    return None


def scrape_noticia(html_content):
    selector = parsel.Selector(text=html_content)

    seletected = selector.css(".tec--toolbar__item *::text").getall()

    output = {
        "url": selector.css('link[rel="canonical"]::attr(href)').get(),
        "title": selector.css("#js-article-title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": extract_writer(selector),
        "shares_count": extract_count(seletected, r"(\d+) Compartilharam"),
        "comments_count": extract_count(seletected, r"(\d+) Comentários"),
        "summary": "".join(
            selector.css(".tec--article__body > p:first-child ::text").getall()
        ),
        "sources": list(
            map(
                str.strip,
                selector.css(".z--mb-16 div a::text").getall(),
            )
        ),
        "categories": list(
            map(str.strip, selector.css("#js-categories a::text").getall())
        ),
    }
    return output


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
