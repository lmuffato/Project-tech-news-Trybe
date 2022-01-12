from ..database import db
import re


# Requisito 6
def search_by_title(title):
    found_news = db.news.find({"title": {"$regex": title, "$options": 'i'}})
    return [
        (news['title'], news['url'])
        for news in found_news
    ] or []


# Requisito 7
def search_by_date(date):
    date_string_pattern = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def verifyDate():
        if date[5:7] == '02' and int(date[8:]) > 28:
            return False
        elif int(date[5:7]) > 12:
            return False
        else:
            return True
    if not re.fullmatch(date_string_pattern, date) or not verifyDate():
        raise ValueError('Data inválida')
    found_news = db.news.find({"timestamp": {"$regex": date}})
    return [
        (news['title'], news['url'])
        for news in found_news
    ] or []


# Requisito 8
def search_by_source(source):
    found_news = db.news.find({"sources": {"$regex": source, "$options": 'i'}})
    return [
        (news['title'], news['url'])
        for news in found_news
    ] or []


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
