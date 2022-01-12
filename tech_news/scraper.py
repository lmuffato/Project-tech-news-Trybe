from requests import get
from time import sleep
from bs4 import BeautifulSoup
import requests
from tech_news.database import create_news


def fetch(url):
    sleep(1)
    response = None
    try:
        response = get(url, timeout=3)
        if (response.status_code == 200):
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    returnList = []
    readed = BeautifulSoup(html_content)
    div = readed.find('div', attrs={'class': "tec--list--lg"})
    if div is None:
        return returnList
    test = div.find_all_next('a', attrs={'class': "tec--card__thumb__link"})
    for a in test:
        returnList.append(a.get('href'))
    return returnList


# Requisito 3
def scrape_next_page_link(html_content):
    readed = BeautifulSoup(html_content)
    a = readed.find('a', 'tec--btn')
    if a is None:
        return None
    link = a.get('href')
    return link


# Requisito 4
def scrape_noticia(html_content):
    readed = BeautifulSoup(html_content)
    divs = readed.find_all('div')
    mapedDivs = list(map(lambda div: div.get_text(), divs))
    filteredDivs = list(filter(lambda div: 'Compartilharam' in div, mapedDivs))
    shareCount = 0
    if len(filteredDivs) > 0:
        shareCount = filteredDivs[-1].strip().split(' ')[0]
    comment = readed.find('button', attrs={'id': 'js-comments-btn'})
    rawSources = readed.find_all('a', attrs={'rel': 'noopener nofollow'})
    categories = readed.find_all('a', 'tec--badge tec--badge--primary')
    refindedSources = list(map(lambda a: a.get_text().strip(), rawSources))

    def filterDef(str):
        v1 = len(str) >= 2 and 'preço' not in str
        digit = str.replace(',', '', 1).replace('.', '', 1)
        v2 = not digit.isdigit() and '$' not in str
        if not v1 or not v2:
            return False
        return True
    filterdeSources = list(filter(filterDef, refindedSources))
    url = readed.find('meta', attrs={'property': 'og:url'}).get('content')
    writers = list(filter(lambda a: 'autor' in a.get('href'),
                                    readed.find_all('a')))
    filteredWirters = list(filter(lambda a: len(a.get_text()) > 3, writers))
    filterTecMundo = list(filter(lambda txt: 'tec_mundo' not in txt,
                                             filterdeSources))
    article = readed.find('div', 'tec--article__body')
    summary = article.find('p').get_text()
    returnDict = {
        'timestamp': readed.find('time').get('datetime'),
        'url': url,
        'title': readed.find('h1').get_text(),
        'shares_count': int(shareCount),
        'comments_count': int(comment.get('data-count')),
        'summary': summary,
        'sources': filterTecMundo,
        'categories': list(map(lambda a: a.get_text().strip(), categories)),
    }
    if len(writers) != 0:
        returnDict['writer'] = filteredWirters[0].get_text().strip()
    else:
        returnDict['writer'] = 'Equipe TecMundo'
    return returnDict


# Requisito 5
def get_tech_news(amount):
    newsList = []
    baseUrl = 'https://www.tecmundo.com.br/novidades'
    nextLinks = ''
    while len(newsList) < amount:
        newsLink = []
        if len(nextLinks) == 0:
            newsLink = scrape_novidades(fetch(baseUrl))
            nextLinks = scrape_next_page_link(fetch(baseUrl))
        else:
            newsLink = scrape_novidades(fetch(nextLinks))
            nextLinks = scrape_next_page_link(fetch(nextLinks))
        for link in newsLink:
            if len(newsList) < amount:
                newsList.append(scrape_noticia(fetch(link)))
    create_news(newsList)
    print(len(newsList))
    print(newsList[0])
    return newsList
