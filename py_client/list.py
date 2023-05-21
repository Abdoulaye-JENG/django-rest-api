import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
password = getpass()
credentials = {"email": "staff@drf.com", "password": password}
auth_response = requests.post(auth_endpoint, json=credentials)
print(f"!! AUTH Response:: {auth_response.json()}")
if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {"Authorization": f"Klink {token}"}

    endpoint = "http://localhost:8000/api/products/"
    get_response = requests.get(endpoint, headers=headers)

    print("Response JSON: ")
    print(get_response.json())
    print(f"Response Status code: {get_response.status_code}")
