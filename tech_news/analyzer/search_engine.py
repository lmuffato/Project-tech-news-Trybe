from tech_news.database import search_news
from datetime import datetime
import re


def map_answer(news_list):
    return [(x["title"], x["url"]) for x in news_list]


# Requisito 6
def search_by_title(title):
    return map_answer(
        search_news({"title": {"$regex": title, "$options": "i"}})
    )


# Requisito 7
def parse_date(date):
    try:
        regex = re.search(r"(\d{4})-(\d{2})-(\d{2})", date)
        year, month, day = regex.groups()
        return datetime(int(year), int(month), int(day)).isoformat()
    except AttributeError:
        raise ValueError("Data inválida")
    except ValueError:
        raise ValueError("Data inválida")


def search_by_date(date):
    parse_date(date)
    return map_answer(search_news({"timestamp": {"$regex": date}}))


# Requisito 8
def search_by_source(source):
    return map_answer(
        search_news(
            {"sources": {"$elemMatch": {"$regex": source, "$options": "i"}}}
        )
    )


# Requisito 9
def search_by_category(category):
    return map_answer(
        search_news(
            {
                "categories": {
                    "$elemMatch": {"$regex": category, "$options": "i"}
                }
            }
        )
    )
