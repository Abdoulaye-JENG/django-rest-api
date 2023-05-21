import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Client Product N° 5 (Trough mixins)",
    "content": "Client Product [5] content.",
}

get_response = requests.post(endpoint, json=data)

print("Response JSON: ")
print(get_response.json())
print(f"Response Status code: {get_response.status_code}")
