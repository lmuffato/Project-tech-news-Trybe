def get_shares_count(selector):
    shares_count = selector.css(
        "#js-author-bar > nav >"
        "div:nth-child(1)::text"
        ).get()

    if shares_count is None or not ('Compartilharam'):
        shares_count = 0

    return shares_count


def get_comments(selector):
    comments_count = selector.css("#js-comments-btn ::text").get()
    if comments_count is None:
        comments_count = 0

    return comments_count


def get_summary(selector):  
    summary = selector.css(
        "div.tec--article__body-grid > "
        "div.tec--article__body.z--px-16.p402_premium *::text"
        ).get()

    return summary


def get_sources(selector):
    arr = []
    sources = selector.css(
        "article > div.tec--article__body-grid"
        "> div.z--mb-16.z--px-16 > div ::text"
        ).getall()

    for source in sources:
        arr.append(source.split())

    return sources


def get_categories(selector):
    arr = []
    categories = selector.css(
            "#js-categories ::text"
            ).getall()

    for cat in categories:
        arr.append(cat.strip())
    return arr
