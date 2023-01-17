import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from pprint import pprint
import re
import json
import codecs

HOST = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
headers = Headers(browser='firefox', os= 'win').generate()

html = requests.get(HOST, headers= headers).text

# print(html) 

soup = BeautifulSoup(html, features='lxml')

vacancy_list = soup.find(class_ = 'vacancy-serp-content')

vacancy_card = soup.find_all(class_ = 'vacancy-serp-item__layout')

json_list =[]

for vacancy in vacancy_card:
    link_tag = vacancy.find('a', class_='serp-item__title')
    link = link_tag['href']
    wages_tag = vacancy.find('span', class_='bloko-header-section-3')
    if wages_tag != None:
        wages = wages_tag.text
    else:
        wages = "Зароботная плата не указана"
    print(wages)
    company_name_tag = vacancy.find('a', class_='bloko-link bloko-link_kind-tertiary')
    company_name = company_name_tag.text
    print(company_name)
    city_tag = vacancy.find('div', class_="vacancy-serp-item__info")
    city_tag1 = city_tag.find_all('div', class_="bloko-text")
    city = re.findall(r'(^\w+-?\w+)(,?.+)?', (city_tag1[1].text))[0][0]
    print(city)
    vacancy_html = requests.get(link, headers= headers).text
    vacancy_soup = BeautifulSoup(vacancy_html, features='lxml')
    vacancy_desc_tag = vacancy_soup.find('div', class_ = 'bloko-columns-row')
    vacancy_desc = vacancy_desc_tag.text
    if 'Flask' in vacancy_desc and 'Django' in vacancy_desc:
        vacancy_dic = {'link': link, 'wages': wages, 'company_name': company_name, 'city': city}
        json_list.append(vacancy_dic)

    
with open("vacancy.json", "w", encoding="utf-8") as file:
    json.dump(json_list, file, indent=4)
print(json_list)