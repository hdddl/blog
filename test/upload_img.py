# coding=utf-8
import requests

url = "http://localhost:8000/img/upload"

name = 'file.png'
album = "wallpaper"
client = requests.Session()

r1 = client.get(url)
csrf_token = r1.cookies['csrftoken']

upload_files = {
    'image': open(name, 'rb'),
}

upload_data = {
    'csrfmiddlewaretoken': csrf_token,
    'name': name,
    'album': "1",
}

resp = client.post(url,files=upload_files ,data=upload_data, headers=dict(Referer=url))

if resp.status_code == 200:
    print(resp.json())
else:
    print(resp.status_code)
