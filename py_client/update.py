import requests

endpoint = "http://localhost:8000/api/products/8/update/"

data = {"title": "Updated Title", "content": "Updated Content"}
response = requests.put(endpoint, json=data)

print("Response: ")
print(response.json())
