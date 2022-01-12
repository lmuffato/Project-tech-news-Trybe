from requests import get
from time import sleep
from bs4 import BeautifulSoup
import requests


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
    shareCount = readed.find('button', attrs={'id': 'js-comments-btn'})
    comment = readed.find('button', attrs={'id': 'js-comments-btn'})
    rawSources = readed.find_all('a', attrs={'rel': 'noopener nofollow'})
    categories = readed.find_all('a', 'tec--badge tec--badge--primary')
    refindedSources = list(map(lambda a: a.get_text().strip(), rawSources))
    filterdeSources = list(filter(lambda str: len(str) >= 2, refindedSources))
    url = readed.find('meta', attrs={'property': 'og:url'}).get('content')
    writers = list(filter(lambda a: 'autor' in a.get('href'),
                                    readed.find_all('a')))
    filteredWirters = list(filter(lambda a: len(a.get_text()) > 3, writers))
    filterTecMundo = list(filter(lambda txt: 'tec_mundo' not in txt,
                                             filterdeSources))
    summary = readed.find('meta', attrs={'name': 'description'}).get('content')
    returnDict = {
        'timestamp': readed.find('time').get('datetime'),
        'url': url,
        'title': readed.find('h1').get_text(),
        'shares_count': int(shareCount.get('data-count')),
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
    """Seu código deve vir aqui"""
