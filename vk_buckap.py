import requests
import json
from datetime import datetime
from pprint import pprint

access_token = 'vk1.a.qRi20dh3_LAbKYye68ARXPgE1ZDJ8_qr0aEEPbN2vJgYYtnWwHEmBUkI2VlthNDTF7pXvOhTKfJHyQDBcdoquJpf0JP_ZHovaP0KcnSZbTlbEwrI6k4yPln3oM9kBwA4X46TtIyj40XeiwduW7ML_DmdfPCD3T9nIRaWZi8lrMw92ze3Bb3IkYj6-qQadqwCGh1Bzz2MlKGXrVxyXnxYxg'
user_id = '29661444'

class VK:

    def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}


    def vk_photo(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'album_id': 'profile', 'extended': '1', 'rev': '1', 'count': '5'}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

vk = VK(access_token, user_id)
# pprint(vk.vk_photo())

with open ("table.json", "w", encoding= "utf-8") as file:
    json_list =[]
    items_photo = vk.vk_photo()['response']['items']
    # print(len(items_photo))
    for item in items_photo:
        name_photo = str(item['likes']['count']) + '.jpg'
        # print(name_photo_like)
        if len(json_list) > 0:
            for dic in json_list:
                if name_photo == dic['file_name']:
                    data_vk = str(datetime.utcfromtimestamp(item['date']).strftime("%d.%m.%Y"))
                    name_photo = f'{name_photo}_{data_vk}'
                    sizes = item['sizes'][-1]['type']  
                    json_list.append({'file_name': name_photo, 'size': sizes})          
                else:
                    sizes = item['sizes'][-1]['type']
                    json_list.append({'file_name': name_photo, 'size': sizes})
        else:
            sizes = item['sizes'][-1]['type']
            json_list.append({'file_name': name_photo, 'size': sizes})
        json.dump(json_list, file, indent=4)
        print(json_list)





    