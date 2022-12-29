import requests
import json
from datetime import datetime

TOKEN = 


class VK:

    def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
       url = 'https://api.vk.com/method/users.get'
       params = {'user_ids': self.id}
       response = requests.get(url, params={**self.params, **params})
       return response.json()

    def vk_photo(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'album_id': 'profile', 'extended': '1', 'rev': '1', 'count': '5'}
        response = requests.get(url, params={**self.params, **params})
        return response.json()



access_token = 'vk1.a.qRi20dh3_LAbKYye68ARXPgE1ZDJ8_qr0aEEPbN2vJgYYtnWwHEmBUkI2VlthNDTF7pXvOhTKfJHyQDBcdoquJpf0JP_ZHovaP0KcnSZbTlbEwrI6k4yPln3oM9kBwA4X46TtIyj40XeiwduW7ML_DmdfPCD3T9nIRaWZi8lrMw92ze3Bb3IkYj6-qQadqwCGh1Bzz2MlKGXrVxyXnxYxg'
user_id = '29661444'
vk = VK(access_token, user_id)
# print(vk.users_info())

def homework():
    with open("result.json", "w", encoding='utf-8') as file:
        results = list()
        items = vk.vk_photo()['response']['items']
        items_amt = len(items)
        print(f'Всего {items_amt} фото')
        for item in items:
            file_name = str(item['likes']['count']) + '.jpg'
            if len(results) > 0:
                for result in results:
                    if file_name == result['file_name']:
                        file_name = file_name[:-4] + '_{0}'.format(str(datetime.utcfromtimestamp(item['date']).strftime("%d.%m.%Y %H:%M:%S"))) + '.jpg'
            else:
                file_name = file_name
            size = item['sizes'][-1]['type']
            url = item["sizes"][-1]['url']
            yadisk(url)
            results.append({'file_name': file_name, 'size': size})
        json.dump(results, file, indent=4)

def yadisk(url):
    pass