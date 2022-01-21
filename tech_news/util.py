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
        "div.tec--article__body.z--px-16.p402_premium > p:nth-child(1) ::text"
        ).get()

    return summary


def get_sources(selector):
    sources = selector.css(
        "article > div.tec--article__body-grid"
        "> div.z--mb-16.z--px-16 > div > a:nth-child(1) ::text"
        ).getall()

    return sources


def get_categories(selector):
    categories = selector.css(
            "#js-categories > a:nth-child(1) ::text"
            ).getall()

    return categories
