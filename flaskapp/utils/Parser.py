from flaskapp.utils.definition_scraper import get_definitions
from flaskapp.utils.stocks import is_ticker

class Parser:

    def __init__(self):
        self.article = ""
        self.definitions = get_definitions()
        self.response = {}

    def get_keywords(self):
        return self.response

    def azure_parse(self):
        return

    def dictonary_parse(self):
        article_split = self.article.split(' ')
        for i in range(len(article_split)):
            if article_split[i] in self.definitions:
                word = article_split[i]
                self.response[word] = {
                    "type": "definition",
                    "definition": self.definitions[word],
                    "location": i
                }
            elif is_ticker(article_split[i]):
                ticker = article_split[i]
                self.response[ticker] = {
                    "type": "ticker",
                    "ticker": ticker,
                    "location": i,
                    "analysis": 'BLACKROCK ANALYSIS'
                }

    def set_article(self, article):
        self.article = article.lower()

    def get_article(self):
        return self.article

    def get_definitions(self):
        return self.definitions

if __name__ == '__main__':
    parser = Parser()
    parser.set_article("the djia fell lots today. AMZN is doing great! And how are we all doing. I am fansaotiaidb aosidja awh o")
    parser.dictonary_parse()
    print(parser.response)

