import requests
import json

Base = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "video/1", "views": 10000},
        {"likes": 20, "name": "video/2", "views": 23434},
        {"likes": 1, "name": "video/3", "views": 1}]

for i in range(len(data)):
    response = requests.put(Base + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(Base + "video/2")
print(response.json())
