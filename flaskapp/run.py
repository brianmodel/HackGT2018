from flask import Flask, request
from flaskapp.utils.summarizer import create_summary
from flaskapp.utils.definition_scraper import get_definitions
app = Flask(__name__)

@app.route('/summary')
def get_summary():
    article = request.headers['Article']
    summary = create_summary(article)
    return summary

@app.route('/keywords')
def get_keywords():
    return

@app.route('/blackrock/<ticker>')
def get_blackrock_analysis(ticker):
    url = "https://www.blackrock.com/tools/hackathon/portfolio-analysis?calculateExposures=true&calculatePerformance=true&positions="+ticker+"~100"
    requests.get(url)