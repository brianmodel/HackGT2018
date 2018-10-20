import requests
from bs4 import BeautifulSoup
import pickle

def get_definitions():
    '''
    returns the dictionary of financial definitions
    :return:
    '''
    with open('serialized/definitions.pickle', 'rb') as handle:
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

        print('finished one')
        with open('definitions' + str(num) + '.pickle', 'wb') as handle:
            pickle.dump(definitions, handle)
        num+=1

    with open('definitions.pickle', 'wb') as handle:
        pickle.dump(definitions, handle)

if __name__ == '__main__':
    get_data()
