from pprint import pprint

from bs4 import BeautifulSoup as bs
import requests
import fake_headers
import json


url = "https://hh.ru/search/vacancy"
params = {
    'area': ['1', '2'],
    'text': ['Django', 'Flask'],
    'per_page': '100',
    'customDomain': '1'
}


def gen_headers():
    headers = fake_headers.Headers()
    return headers.generate()


def get_txt(source):
    data = dict()
    response = requests.get(source, headers=gen_headers(), params=params)
    soup = bs(response.text, 'lxml')
    all_frame = soup.find_all('div', class_='serp-item')
    for frame in all_frame:
        try:
            header = frame.find('span', class_='serp-item__title').text
            salary = frame.find('span', class_='bloko-header-section-2').text.replace('\u202f', " ")
            link = frame.find('a', class_='bloko-link').get('href')
            company_name = frame.find('a', class_='bloko-link bloko-link_kind-tertiary').text.replace('\xa0', " ")
            sity = frame.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text.strip()
            data[header] = []
            data[header].append({
                'salary': salary,
                'url': link,
                'company': company_name,
                'sity': sity
            })
        except AttributeError:
            continue

    return data


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(get_txt(url), f, ensure_ascii=False)

