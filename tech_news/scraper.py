import requests
import time
import parsel


# URL = "https://www.tecmundo.com.br/novidades"
# URL_DETAILS = "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"



# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)

        if response.status_code != 200:
            return None
        else:
            return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# print(fetch(URL))


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    lists = []

    lists = selector.css("h3.tec--card__title a::attr(href)").getall()

    # for item in selector.css(".tec--list__item"):
    #     url = item.css(".tec--card__title__link ::attr(href)").get()
    #     lists.append(url)

    return lists


# html = fetch(URL)
# print(scrape_novidades(html))


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    url = selector.css("a.tec--btn--lg ::attr(href)").get()

    return url


# html = fetch(URL)
# print(scrape_next_page_link(html))

# Requisito 4
def extract_comments(comments):
    if comments is None:
        comments = 0
        return comments
    else:
        comments = int(comments)
        return comments

def extract_paragraph(selector):
    paragraphText = selector.css("div.tec--article__body p:first-child *::text").getall()
 
    phrase_complete = "".join(paragraphText)
    
    return phrase_complete

def extract_categories(selector):
    categoriesFormated = []
    categories = selector.css("a.tec--badge--primary ::text").getall()
    
    for category in categories:
        categoriesFormated.append(category.strip())
    
    return categoriesFormated

def extract_sources(selector):
    sourcesFormated = []
    sources = selector.css("div.z--mb-16 a::text").getall()

    for source in sources:
        sourcesFormated.append(source.strip())

    return sourcesFormated


def extract_writer(selector):
    
    if selector.css(".tec--author__info__link ::text").get():
       writer = selector.css(".tec--author__info__link ::text").get()
       return writer
    if selector.css(".tec--timestamp__item a::text").get():
        writer = selector.css(".tec--timestamp__item a::text").get()
        return writer
    if selector.css(".z--m-none ::text").get():
       writer = selector.css(".z--m-none ::text").get()
       return writer


def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    news_json = []
    url = selector.css("head link[rel=canonical] ::attr(href)").get()
    title = selector.css("h1.tec--article__header__title ::text").get()
    timestamp = selector.css("div.tec--timestamp__item ::attr(datetime)").get()
    writer_tech = extract_writer(selector)
    writer = writer_tech.strip() if writer_tech else None
    shares_count = selector.css("div.tec--toolbar__item ::text").re_first(r'\d+')
    comments = selector.css("button.tec--btn ::attr(data-count)").get()
    comments_count = extract_comments(comments)
    summary = extract_paragraph(selector)
    sources = extract_sources(selector)
    categories = extract_categories(selector)

    news_json = {
      "url":url,
      "title":title,
      "timestamp":timestamp,
      "writer":writer,
      "shares_count":int(shares_count),
      "comments_count":comments_count,
      "summary":summary,
      "sources":sources,
      "categories":categories
    }
    return news_json


# URL_DETAILS = "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
# URL_DETAILS = "https://www.tecmundo.com.br/minha-serie/215168-10-viloes-animes-extremamente-inteligentes.htm"
# html_content = fetch(URL_DETAILS)
# print(scrape_noticia(html_content))


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
