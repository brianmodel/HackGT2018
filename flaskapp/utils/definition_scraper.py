import requests
from bs4 import BeautifulSoup
import pickle

definitions = {}

for i in range(26):
    url = 'https://www.forbes.com/sites/forbesfinancialglossary/2011/07/11/'
    if i < 5:
        url = 'https://www.forbes.com/sites/forbesfinancialglossary/2011/07/12/'
    elif i >= 9:
        url = 'https://www.forbes.com/sites/forbesfinancialglossary/2011/07/10/'
    page = requests.get(url+chr(97+i)).content

    soup = BeautifulSoup(page, 'lxml')
    links = soup.find_all('p')
    for link in links:
        if link.string != '\n':
            print(link)