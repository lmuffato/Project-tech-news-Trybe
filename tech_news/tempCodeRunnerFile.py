import requests
import time
from parsel import Selector
URL_BASE = "https://www.tecmundo.com.br/novidades"


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        else:
            return response
    except requests.ReadTimeout:
        return None


x = fetch(URL_BASE)
print(x.url)