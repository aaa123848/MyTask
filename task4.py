from bs4 import BeautifulSoup
import requests

import argparse
import json

def read_json(path):
    with open(path) as f:
        data = json.load(f)
    return data

def get_data(url, limit):
    res = []
    res_len = 0
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tags = soup.find_all(class_="td DescriptionCell")

    if limit == None:
        limit = 20

    for t in tags:
        res.append(t.find('a').string)
        res_len += 1
        if res_len >= limit:
            break
    return res

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", help="how many data get by order")
    parser.add_argument("--country", help="which country do you want to get")
    parser.add_argument("--other", help="<file name>-<filter name> example countries-Taiwan")
    args = parser.parse_args()
    url = 'https://www.alexa.com/topsites'
    limit = None
    if args.top:
        limit = int(args.top)
    if args.country:
        data = read_json('./json/countries.json')
        country_url = data.get(args.country)
        if country_url == None:
            print("Country Not Exist")
            exit()
        url += "/" + country_url
    if args.other:
        data = read_json('./json/{}.json'.format(args.other.split('-')[0]))
        add_url = data.get(args.other.split('-')[1])
        if add_url == None:
            print("url Not Exist")
            exit()
        url += "/" + add_url

    res = get_data(url, limit)
    print(res)