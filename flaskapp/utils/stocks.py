import requests
import json
import csv
import pickle

def get_analysis(ticker):
    url = "https://www.blackrock.com/tools/hackathon/portfolio-analysis?calculateExposures=true&calculatePerformance=true&positions=" + ticker + "~100"
    response = json.dumps(requests.get(url).json())
    print(response)
    return response

def is_ticker(ticker):
    with open('data/stocks/stocks.pickle', 'rb') as stocks:
        stocks = pickle.load(stocks)
    return ticker in stocks

def parse_stock_data():
    with open("data/stocks/companylist.csv") as stocks:
        csv_reader = csv.reader(stocks, delimiter=',')
        is_first = True
        stocks = []
        for row in csv_reader:
            if is_first:
                is_first = False
                continue
            stocks.append(row[0].lower())

        stocks = set(stocks)

        with open('data/stocks/stocks.pickle', 'wb') as handle:
            pickle.dump(stocks, handle)

        return stocks

    with open('stocks.pickle', 'wb') as handle:
        pickle.dump(definitions, handle)



if __name__ == '__main__':
    data = parse_stock_data()
    print(data)
