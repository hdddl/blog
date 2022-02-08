# coding=utf-8
import requests

url = "http://localhost:8000/img/upload"

name = 'file.png'
album = "wallpaper"

upload_data = {
    "name": (None, name),
    "album": (None, album),
    "image": (name, open(name, 'rb')),
}

r = requests.post(url, files=upload_data)

if r.status_code == 200:
    print("file upload success")
    print(r.json())
else:
    print(r.status_code)
