class NewsConstructor:
    @classmethod
    def format_paragraph(list_of_paragraphs):
        paragraphs = list_of_paragraphs
        return "".join(paragraphs)

    def extract_numbers(phrase):
        if phrase:
            return [int(s) for s in phrase.split() if s.isdigit()][0]
        else:
            return 0
