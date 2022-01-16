# req 4 util
def get_writer(selector):
    writer = selector.css(".z--font-bold *::text").get()
    if writer:
        return writer.strip()
    return None


def get_share_counts(selector):
    counts_string = selector.css(".tec--toolbar__item::text").get()
    if counts_string:
        return int(counts_string.split()[0])
    return 0


def get_comments_counts(selector):
    counts = selector.css("#js-comments-btn::attr(data-count)").get()
    if counts:
        return int(counts)
    return 0


def get_summary(selector):
    summary = selector.css(
        ".tec--article__body > p:nth-child(1) *::text"
    ).getall()
    return "".join(summary)


def get_categories(selector):
    categories_arr = selector.css("#js-categories a::text").getall()
    return categories_arr


def get_sources(selector, categories):
    """uso do filter:
    https://www.pythonpip.com/python-tutorials/how-to-filter-a-list-in-python/
    """
    sources_arr_unfilted = selector.css(".tec--badge::text").getall()
    sources_arr = filter(lambda a: a not in categories, sources_arr_unfilted)
    return list(sources_arr)


def strip_list_intems(list):
    to_return = []
    for item in list:
        to_return.append(item.strip())
    return to_return
