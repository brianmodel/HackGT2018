from definition_scraper import get_definitions
from stocks import is_ticker, get_ticker
from azure_util import entity_linking, key_phrases, sentiment_analysis

class Parser:

    def __init__(self):
        self.article = ""
        self.definitions = get_definitions()
        self.response = {}

    def get_keywords(self):
        self.dictonary_parse()
        return self.response

    def azure_parse(self):
        response = entity_linking(self.article)['documents']
        entities = response[0]['entities']
        for entity in entities:
            name = entity['name']                
            index = entity['matches'][0]['offset']
            wiki = entity['wikipediaUrl']
            self.response[name] = {
                "type": "azureEntity",
                "wikipediaUrl": wiki,
                "index": index
            }
            if get_ticker(name) != None:
                self.response[name] = {
                "type": "azureEntity",
                "wikipediaUrl": wiki,
                "index": index,
                "ticker"L get_ticker(name)
            }


    def dictonary_parse(self):
        article_split = self.article.split(' ')
        words = []
        for key in self.definitions.keys():
            if key in self.article.lower():
                words.append((key, self.article.lower().index(key)))
        for word in words:
            self.response[word[0]] = {
                "type": "definition",
                "definition": self.definitions[word[0]],
                "index": word[1],
            }

        for i in range(len(article_split)):
            if is_ticker(article_split[i]):
                ticker = article_split[i]
                self.response[ticker] = {
                    "type": "ticker",
                    "ticker": ticker,
                    "index": i,
                    "analysis": 'BLACKROCK ANALYSIS'
                }

    def set_article(self, article):
        self.article = article

    def get_article(self):
        return self.article

    def get_definitions(self):
        return self.definitions

if __name__ == '__main__':
    import json
    text = 'After worries about higher interest rates sparked a steep sell-off in early October and again on Thursday, the S & P 500 remains down 5 percent from its Sept. 20 record high close, with top-shelf stocks including Amazon.com Inc(AMZN.O), Alphabet Inc(GOOGL.O), Accounts Payable Netflix Inc(NFLX.O) and Facebook Inc(FB.O) showing little of their vitality from recent years.A quarterly report from Microsoft Corp(MSFT.O) on Wednesday after the bell, followed by Alphabet and Amazon late on Thursday, will influence sentiment across Wall Street.“The equity market is at a critical point here, ” said Kurt Brunner, portfolio manager, Swarthmore Group in Philadelphia, Pennsylvania. “In order for it not to get a lot worse, I think you need to see Amazon and Alphabet put up some good numbers.”With investors worried about increased internet regulation and criticism of Facebook’s handling of user data, the social media company’s stock has slumped 29 percent from its record high on July 25. Alphabet is 15 percent below its July 26 record high close, while Amazon has fallen 12 percent this month.'
    parser = Parser()
    parser.set_article(text)
    # parser.dictonary_parse()
    # print(parser.response)
    parser.azure_parse()
    print(get_ticker('amazon'))

