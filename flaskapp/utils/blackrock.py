import requests
import json
import sys
import requests.packages.urllib3
from datetime import date, time, datetime
from dateutil import parser

requests.packages.urllib3.disable_warnings()


def get_analysis(tick):
    ticker = tick


    # if len(ticker) >= 5:
    #     r = requests.get('http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=' + ticker + '&region=1&lang=en', verify=False)
    #     try:
    #         tickerSym = r.json()['ResultSet']['Result'][0]["symbol"]
    #         tickerName = r.json()['ResultSet']['Result'][0]["name"]
    #         print("it worked")
    #     except:
    #         print("Sorry, I couldn't find the company you were looking for, try asking for a different one.")
    #         exit()
    # else:
    #     r = requests.get('http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=' + ticker + '&region=1&lang=en', verify=False)
    #     tickerSym = ticker
    #     try:
    #         tickerName = r.json()['ResultSet']['Result'][0]["name"]
    #         print("it worked")
    #     except:
    #         print("Sorry, I couldn't find the ticker you were looking for, try asking for a different one.")
    #         exit()

    r = requests.get('http://www.blackrock.com/tools/hackathon/performance?identifiers=' + ticker, verify=False)

    response = r.status_code

    if response == 200:
        doIt = 0

        response = r.json()
        try:
            json_data = response['resultMap']['RETURNS'][0]
        except:
            r = requests.get('http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=' + ticker + '&region=1&lang=en', verify=False)
            try:
                tickerSym = r.json()['ResultSet']['Result'][0]["symbol"]
            except:
                return "Sorry, there was an error getting that data, please try again later."
            else:
                r = requests.get('http://www.blackrock.com/tools/hackathon/performance?identifiers=' + tickerSym, verify=False)
                response = r.status_code
                if response == 200:
                    response = r.json()

                    try:
                        json_data = response['resultMap']['RETURNS'][0]
                    except:
                        return "Sorry, it doesn't look like we have information on that stock."
                    else:
                        doIt = 1
        else:
            doIt = 1

        if doIt == 1:

            if parser.parse(str(json_data['highDate'])) == datetime.today() or parser.parse(str(json_data['highDate'])) == parser.parse("20181018"):
                highTime = 1
            else:
                highTime = 0

            dateString = str(datetime.today().strftime('%Y%m%d'))
            dateString = "20181018"
            returnsMap = json_data["returnsMap"]
            stockInfo = returnsMap[dateString]
            upPercentage = json_data['upMonthsPercent']
            sharpe = stockInfo['oneYearSharpeRatio']
            risk = stockInfo['oneYearRisk']
            totalMonths = json_data['totalMonths']
            returnsType = json_data['returnsType']

            speechOutput = "Here's the BlackRock report on the " + ticker + " stock. "

            if highTime == 1:
                speechOutput += "It's currently at it's highest price. "

            speechOutput += "It typically goes up " + str(round((upPercentage * 100), 2)) + "% of the time, based on the " + str(totalMonths) + " months we have the data for. "

            speechOutput += "It usually offers returns " + returnsType.lower() + ", with a one year return on investment of " + str(round(sharpe,2)) + " and a risk of " + str(round(risk,2)) + "."

            return speechOutput


if __name__ == "__main__":
    print(get_analysis("AMZN"))

