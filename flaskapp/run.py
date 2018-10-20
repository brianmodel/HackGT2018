from flask import Flask, request
from flaskapp.utils.summarizer import create_summary
app = Flask(__name__)

@app.route('/summary')
def get_summary():
    article = request.headers['Article']
    summary = create_summary(article)
    return summary

@app.route('/keywords')
def get_keywords():
    return

