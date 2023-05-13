import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000"

get_response = requests.get(endpoint, json={"query": "Mr Robot"})

print("Response as raw text: ")
print(get_response.text)
print(f"Response Status code: {get_response.status_code}")
