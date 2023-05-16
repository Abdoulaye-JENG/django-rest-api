import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "Hello!"})

print("Response JSON: ")
print(get_response.json())
print(f"Response Status code: {get_response.status_code}")
