def get_url(selector):
    url = selector.css('head link[rel=canonical]::attr(href)').get()
    return url
