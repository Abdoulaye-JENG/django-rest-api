import requests

endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query": "Mr Robot"})

print("Response as raw text: ")
print(get_response.text)

print("Response as JSON")
print(get_response.json())

print(f"Response Status code: {get_response.status_code}")
