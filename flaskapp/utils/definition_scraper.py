#Don't look here apart from get_definitions. Everything else is parsing hell

import requests
from bs4 import BeautifulSoup
import pickle
import os

dirname = os.path.dirname(__file__)

def get_definitions():
    '''
    returns the dictionary of financial definitions
    :return:
    '''
    with open(dirname + '/data/serialized/definitions.pickle', 'rb') as handle:
        b = pickle.load(handle)
    return b

def serialize_data():
    definitions = {}
    num = 0

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
                try:
                    next_link = link.next.attrs['href']
                    next_page = requests.get(next_link).content
                    next_soup = BeautifulSoup(next_page, 'lxml')
                    paragraph = next_soup.find_all('p', class_='speakable-paragraph')[0].string
                    definitions[str(link.string)] = str(paragraph)
                except:
                    continue

        # Storing temporary serialized files in case there is a crash in the program
        with open('definitions' + str(num) + '.pickle', 'wb') as handle:
            pickle.dump(definitions, handle)
        num+=1

    # The beefy boi that contains the full serialized dictionary
    with open('definitions.pickle', 'wb') as handle:
        pickle.dump(definitions, handle)

def edit_dictionary():

    change = []
    definitions = get_definitions()
    for key in definitions.keys():
        if "(" in key:
            words = key.split('(')
            other = words[1][:-1]
            change.append((other, key))

    for i in change:
        definitions[i[0]] = definitions[i[1]]
        first = i[1].split('(')[:-1][0][:-1]
        definition = definitions[i[1]]
        definitions[first] = definition

    with open('data/serialized/definitions.pickle', 'wb') as handle:
        pickle.dump(definitions, handle)

def make_lowercase():
    definitions = get_definitions()
    definitions = {k.lower(): v for k, v in definitions.items()}

    with open('data/serialized/definitions.pickle', 'wb') as handle:
        pickle.dump(definitions, handle)

if __name__ == '__main__':
    print(get_definitions().keys())
