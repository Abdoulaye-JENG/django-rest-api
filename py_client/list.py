import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title": "Cient Product N° 2",
    "content": "Client Product 3 content",
    "price": 27.85,
}
get_response = requests.get(endpoint)

print("Response JSON: ")
print(get_response.json())
print(f"Response Status code: {get_response.status_code}")
