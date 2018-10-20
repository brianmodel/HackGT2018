import requests

subscription_key = "5b68670c6f914f31bcbeaefe27a14ebb"
text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

def entity_linking(article):
    entity_linking_api_url = text_analytics_base_url + "entities"

    documents = {'documents': [
        {'id': '1', 'language': 'en',
            'text': article
         }]
    }
    responseEntities = requests.post(entity_linking_api_url, headers=headers, json=documents)
    entities = responseEntities.json()
    return entities

def key_phrases(article):
    key_phrase_api_url = text_analytics_base_url + "keyPhrases"

    documents = {'documents': [
        {'id': '1', 'language': 'en',
            'text': article
         }]
    }
    responseKeyPhrase = requests.post(key_phrase_api_url, headers=headers, json=documents)
    key_phrases = responseKeyPhrase.json()
    return key_phrases


def sentiment_analysis(article):
    sentiment_analysis_api_url = text_analytics_base_url + "sentiment"

    documents = {'documents': [
        {'id': '1', 'language': 'en',
            'text': article
         }]
    }
    responseSentiment = requests.post(sentiment_analysis_api_url, headers=headers, json=documents)
    sentiment = responseSentiment.json()
    return sentiment

if __name__ == '__main__':
    from pprint import pprint

    a = entity_linking('Microsoft released Windows 10.')
    b = key_phrases("In 1975, Bill Gates III and Paul Allen founded the company.")
    c = sentiment_analysis('Hello world. This is some input text that I love.')

    pprint(a)
    print("====================================================================================================")
    pprint(b)
    print("====================================================================================================")
    pprint(c)
    print("====================================================================================================")