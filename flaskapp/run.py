from flask import Flask, request, jsonify
from flaskapp.utils.summarizer import create_summary
from flaskapp.utils.Parser import Parser
from flaskapp.utils.stocks import get_analysis
app = Flask(__name__)

parser = Parser()

@app.route('/summary')
def get_summary():
    article = request.headers['Article']
    summary = create_summary(article)
    return summary

@app.route('/keywords')
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
    article = request.headers['Article']
    parser.set_article(article)
    return jsonify(parser.get_keywords())

@app.route('/blackrock/<ticker>')
def get_blackrock_analysis(ticker):
    return get_analysis(ticker)

if __name__ == '__main__':
    parser = Parser()
    parser.set_article("dank memes")
    a = parser.get_definitions()
    print(a)