import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/95454545454"

get_response = requests.get(endpoint)

print("Response JSON: ")
print(get_response.json())
print(f"Response Status code: {get_response.status_code}")
