from flaskapp.utils.definition_scraper import get_definitions

class Parser:

    def __init__(self):
        self.article = ""
        self.definitions = get_definitions()
        self.response = {}

    def get_keywords(self):
        return

    def azure_parse(self):
        return

    def dictonary_parse(self):
        article_split = self.article.split(' ')
        for i in range(len(article_split)):
            if article_split[i] in self.definitions:
                word = article_split[i]
                self.response[word] = {
                    "type": "definition",
                    "location": i
                }

    def set_article(self, article):
        self.article = article.lower()

    def get_article(self):
        return self.article

    def get_definitions(self):
        return self.definitions

if __name__ == '__main__':
    parser = Parser()
    parser.set_article("djia fell lots today")
    parser.dictonary_parse()
    print(parser.response)

