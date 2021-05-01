from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.alexa.com/topsites/countries'

r = requests.get(url)
res = {}
soup = BeautifulSoup(r.text, 'html.parser')
for span in soup.find_all(class_='countries span3'):
    for li in span.find_all('li'):
        res[li.find('a').string] = li.find('a').get('href')

with open('./json/countries.json', 'w') as jsonfile:
    json.dump(res, jsonfile)
