import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {"userId": "1", "title": "foo", "body": "bar"}

response = requests.post(url, data=data)

print(response.status_code)

print(response.json())
