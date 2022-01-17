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
