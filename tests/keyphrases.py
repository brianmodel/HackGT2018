import requests
from pprint import pprint

subscription_key = "5b68670c6f914f31bcbeaefe27a14ebb"
assert subscription_key
text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
key_phrase_api_url = text_analytics_base_url + "keyPhrases"
print(key_phrase_api_url)
entity_linking_api_url = text_analytics_base_url + "entities"
print(entity_linking_api_url)

documents = {'documents': [
    {'id': '1', 'language': 'en',
        'text': 'After worries about higher interest rates sparked a steep sell-off in early October and again on Thursday, the S & P 500 remains down 5 percent from its Sept. 20 record high close, with top-shelf stocks including Amazon.com Inc(AMZN.O), Alphabet Inc(GOOGL.O), Netflix Inc(NFLX.O) and Facebook Inc(FB.O) showing little of their vitality from recent years.A quarterly report from Microsoft Corp(MSFT.O) on Wednesday after the bell, followed by Alphabet and Amazon late on Thursday, will influence sentiment across Wall Street.“The equity market is at a critical point here, ” said Kurt Brunner, portfolio manager, Swarthmore Group in Philadelphia, Pennsylvania. “In order for it not to get a lot worse, I think you need to see Amazon and Alphabet put up some good numbers.”With investors worried about increased internet regulation and criticism of Facebook’s handling of user data, the social media company’s stock has slumped 29 percent from its record high on July 25. Alphabet is 15 percent below its July 26 record high close, while Amazon has fallen 12 percent this month.'},
    {'id': '2', 'language': 'en',
        'text': 'BRUSSELS/SAN FRANCISCO(Reuters) - Alphabet Inc’s(GOOGL.O) Google will charge hardware firms up to $40 per device to use its apps under a new licensing system to replace one that the European Union this year deemed anti-competitive, a person familiar with the matter said on Friday. The new fee goes into effect on Oct. 29 for any new smartphone or tablet models launched in the European Economic Area and running Google’s Android operating system, the company announced on Tuesday. The fee can be as low as $2.50 and rises depending on the country and device size, the person said. It is standard across manufacturers, with the majority likely to pay around $20, the person added.'}
]}
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
responseKeyPhrase = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = responseKeyPhrase.json()
pprint(key_phrases)
print("=============================================================================================================================")
responseEntities = requests.post(entity_linking_api_url, headers=headers, json=documents)
entities = responseEntities.json()
pprint(entities)
