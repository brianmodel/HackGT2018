import requests
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

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

def stockPrice(ticker):
    url = "https://api.iextrading.com/1.0/stock/" + ticker + "/batch?types=quote,news,chart&range=1y&last=10"
    response = requests.get(url).json()["quote"]["latestPrice"]

    return response

def generateChart(ticker):
    dates = []
    prices = []
    url = "https://api.iextrading.com/1.0/stock/" + ticker + "/chart/1y"
    response = requests.get(url).json()
    for entry in response:
        del entry["open"]
        del entry["high"]
        del entry["low"]
        del entry["volume"]
        del entry["unadjustedVolume"]
        del entry["change"]
        del entry["changePercent"]
        del entry["vwap"]
        del entry["changeOverTime"]

    for point in response:
        dates.append(point["date"])
        prices.append(point["close"])

    return [dates, prices]


if __name__ == "__main__":
    print(generateChart("GOOGL"))




