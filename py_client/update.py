import requests

endpoint = "http://localhost:8000/api/products/4/update/"

data = {
    "title": "$Mixins product title update",
    "content": "$Mixins product content update",
    "price": 44.99,
}
response = requests.put(endpoint, json=data)

print("Response: ")
print(response.json())
