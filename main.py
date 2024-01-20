from bs4 import BeautifulSoup as bs
import requests
import fake_headers
import pprint

url = "https://hh.ru/search/vacancy"
params = {
    'area': '1',
    'text': 'Django'
}


def gen_headers():
    headers = fake_headers.Headers()
    return headers.generate()


def get_txt(source):
    response = requests.get(source, headers=gen_headers(), params=params).text
    soup = bs(response, 'lxml')
    all_frame = soup.find_all('div', class_='serp-item')
    for frame in all_frame:
        soup.find('div', class_='vacancy-serp-item__layout')

        print(frame.text)

get_txt(url)