import pprint

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

params = {
    "userId": "1",
}

response = requests.get(url, params=params)

data = response.json()

pprint.pprint(data)
