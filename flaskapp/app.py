from flask import Flask, request, jsonify
from utils.summarizer import create_summary
from utils.Parser import Parser
from utils.stocks import get_analysis
app = Flask(__name__)

parser = Parser()

@app.route('/summary', methods = ['POST'])
def get_summary():
    article = request.data['article']
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
    article = request.data['paragraph']
    parser.set_article(article)
    return jsonify(parser.get_keywords())

@app.route('/blackrock/<ticker>')
def get_blackrock_analysis(ticker):
    return get_analysis(ticker)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)