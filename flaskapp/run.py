from flask import Flask, request
app = Flask(__name__)

@app.route('/summary')
def get_summary():
    '''

    :return:
    '''
    article = request.headers['Article']
    summary = ""
    return summary