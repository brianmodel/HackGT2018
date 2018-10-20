import requests

def related_articles (source = 'reuters', query = "market investors"):

    url = ('https://newsapi.org/v2/everything?'
            'sources=' + source + '&'
            'q=' + query + '&'
            'sortBy=popularity&'
            'apiKey=f7c0b448992c42a7b5b26628938c6b06')

    response = requests.get(url)

    articles = response.json()["articles"][0:5]

    for article in articles:
        del article["source"]
        del article["description"]
        del article["content"]
    return articles
