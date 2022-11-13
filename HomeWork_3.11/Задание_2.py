import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'aplication/json', 'Authorization': f'OAuth {self.token}'}

    def upload_link(self, path_to_file: str):
        upload_url = "https://dev.yandex.net/disk-polygon/?lang=ru&tld=ru#!/v147disk47resources/GetResourceUploadLink"
        headers = self.get_headers()
        perams = {"path": path_to_file, "overwtite": "true"}
        response = requests.get(upload_url, headers=headers, perams=perams)
        return response.json()

    def upload(self, path_to_file):
        result = self.upload_link(path_to_file=path_to_file)
        href = result.get("href", "")
        filename = os.path.basename(path_to_file)
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 210:
            print("Выполено")



if __name__ == '__main__':
    path_to_file = os.path.abspath('test/test.txt')
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)