import pprint

import requests

url = "https://api.github.com"

params = {
    "q": "language:html",
}

response = requests.get(url)

data = response.json()

pprint.pprint(data)
