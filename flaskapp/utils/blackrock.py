import requests
import json

def get_analysis(ticker):
    url = "https://www.blackrock.com/tools/hackathon/portfolio-analysis?calculateExposures=true&calculatePerformance=true&positions=" + ticker + "~100"
    response = json.dumps(requests.get(url).json())
    print(response)


if __name__ == '__main__':
    get_analysis("AAPL")