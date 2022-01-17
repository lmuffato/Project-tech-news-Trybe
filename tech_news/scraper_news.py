def get_url(selector):
    url = selector.css('head link[rel=canonical]::attr(href)').get()
    return url


def get_title(selector):
    title = selector.css('.tec--article__header__title::text').get()
    return title
