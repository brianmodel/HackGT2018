from flaskapp.utils.definition_scraper import get_definitions

class Parser:
    def __init__(self, article):
        self.article = article
        self.definitions = get_definitions()

    def get_keywords(self):
        return

    def azure_parse(self):
        return

    def dictonary_parse(self):
        return