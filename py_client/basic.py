import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

params = {"product_id": 25}
get_response = requests.get(endpoint, params=params, json={"query": "Mr Robot"})

print("Response as raw text: ")
# print(get_response.text)
print(get_response.json())
print(f"Response Status code: {get_response.status_code}")
