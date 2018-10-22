from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.summarizer import create_summary
from utils.Parser import Parser
from utils.stocks import get_analysis
from utils.sentiment import analyze_sentiment
from utils.article_timeline import related_articles, stockPrice, generateChart 

app = Flask(__name__)
CORS(app)

parser = Parser()

@app.route('/summary', methods = ['POST'])
def get_summary():
    article = request.form['article']
    summary = create_summary(article)
    return summary

@app.route('/keywords', methods = ['POST'])
def get_keywords():
    '''
    :return: Json response of keywords, as well as what other features should be assocated with them
    example:
    {
        "GDP": {
            "type": "definition",
            "definition": definition
        },
        "AMZN": {
            "type": stock,
            "currentPrice": price,
            "blackrockData": blackrockdata
        }
    }
    '''
    article = request.form['paragraph']
    parser.set_article(article)
    return jsonify(parser.get_keywords())

@app.route('/blackrock/<ticker>')
def get_blackrock_analysis(ticker):
    return get_analysis(ticker)

@app.route('/sentiment', methods = ['POST'])
def get_sentiment():
    paragraph = request.form['paragraph']
    sentiment = float(analyze_sentiment(paragraph)) >= .5
    return jsonify(int(sentiment))

@app.route('/related')
def get_related_articles():
    return jsonify(related_articles())

@app.route('/stockprice/<ticker>')
def get_stock_price(ticker):
    return jsonify(stockPrice(ticker))

@app.route('/chartdata/<ticker>')
def get_chart_data(ticker):
    return jsonify(generateChart(ticker))

if __name__ == '__main__':
    app.run(host='localhost', port=5000)