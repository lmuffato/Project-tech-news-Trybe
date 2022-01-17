import re


def get_url(selector):
    url = selector.css('head link[rel=canonical]::attr(href)').get()
    return url


def get_title(selector):
    title = selector.css('.tec--article__header__title::text').get()
    return title


def get_timestamp(selector):
    datetime = '.tec--timestamp__item time::attr(datetime)'
    timestamp = selector.css(datetime).get()
    return timestamp


def get_summary(selector):
    summaries = 'div.tec--article__body > p:nth-child(1) *::text'
    summary = selector.css(summaries).getall()
    return ''.join(summary)


def get_writer(selector):

    writers = [
        '.tec--timestamp:nth-child(1) a::text',
        '.tec--author__info p:first-child::text',
        '.tec--author__info p:first-child a::text',
    ]

    selector_writers = []
    for author_selector in writers:
        selected_writers = selector.css(author_selector).get()
        if selected_writers is not None:
            selector_writers.append(selected_writers.strip())
        if selected_writers is None:
            selector_writers.append(None)

    author = [writer for writer in selector_writers if writer]
    if len(author) == 0:
        return None
    return author[0]


def get_shares_count(selector):
    share = selector.css('.tec--toolbar div:first-child::text').get()
    if share is None or not ('Compartilharam') in share:
        return 0
    count_shares = re.findall(r"\s(\d*)\s(...*)", share)
    return int(count_shares[0][0])
