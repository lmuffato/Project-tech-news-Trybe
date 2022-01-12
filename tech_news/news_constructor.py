class NewsConstructor:
    def format_paragraph(list_of_paragraphs):
        paragraphs = list_of_paragraphs
        return "".join(paragraphs)

    def extract_numbers(phrase):
        if phrase:
            return [int(s) for s in phrase.split() if s.isdigit()][0]
        else:
            return 0

    def extract_news_url(element):
        if element:
            return element.xpath(
                '//meta[contains(@property, "url")]').xpath('@content').get()
        else:
            return None

    def extract_news_title(element):
        if element:
            return element.css('h1.tec--article__header__title::text').get()
        else:
            return None

    def get_news_author(element):
        if element:
            writer = element.css('.z--font-bold ::text').get()
            if writer:
                return writer.strip()
            else:
                return writer

    def get_news_summary(element):
        if element:
            summary_paragraph = element.css(
                '.tec--article__body > p:first_child *::text').getall()
            if summary_paragraph:
                return "".join(summary_paragraph).strip()

    def format_strings(str_list):
        key = 0
        list_formatted = []
        while key < len(str_list):
            list_item = str_list[key].strip()
            list_formatted.append(list_item)
            key += 1
        return list_formatted

    @classmethod
    def get_news_categories(cls, element):
        if element:
            categories_list = element.xpath(
                '//div[contains(@id, "js-categories")]'
            ).xpath('./a/text()').getall()
            return cls.format_strings(categories_list)

    @classmethod
    def get_news_sources(cls, element):
        if element:
            sources_list = element.css(
                'div.z--mb-16').xpath('./div/a//text()').getall()
            return cls.format_strings(sources_list)

    @classmethod
    def get_comments_count(cls, element):
        if element:
            comments_count = element.xpath(
                '//button[contains(@id, "js-comments-btn")]').css(
                    '*::text').getall()[1]
            return cls.extract_numbers(comments_count)

    @classmethod
    def get_shares_count(cls, element):
        if element:
            shares_count = element.css('.tec--toolbar__item::text').get()
            return cls.extract_numbers(shares_count)

    def get_datetime(element):
        if element:
            return element.xpath('//time//@datetime').get()

# Source:
# Função extract_numbers adaptada de:
# https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
