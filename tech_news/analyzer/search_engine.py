from datetime import datetime
from tech_news.database import db


# Requisito 6
def search_by_title(title):
    news = list(
        db.news.find(
            {"title": {"$regex": title, "$options": "i"}},
            {"_id": False, "title": True, "url": True},
        )
    )
    return parse_news(news)


# Requisito 7
def search_by_date(date):
    validate_date(date)

    news = list(
        db.news.find(
            {"timestamp": {"$regex": date}},
            {"_id": False, "title": True, "url": True},
        )
    )

    return parse_news(news)


# Requisito 8
def search_by_source(source):
    news = list(
        db.news.find(
            {"sources": {"$regex": source, "$options": "i"}},
            {"_id": False, "title": True, "url": True},
        )
    )

    return parse_news(news)


# Requisito 9
def search_by_category(category):
    news = list(
        db.news.find(
            {"categories": {"$regex": category, "$options": "i"}},
            {"_id": False, "title": True, "url": True},
        )
    )

    return parse_news(news)


def parse_news(news):
    return [(new["title"], new["url"]) for new in news]


def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
