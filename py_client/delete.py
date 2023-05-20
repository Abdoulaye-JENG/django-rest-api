import requests

endpoint = "http://localhost:8000/api/products/7/delete/"

response = requests.delete(endpoint)

print("Delete request response: ")
print(f"code: {response.status_code} -- deleted: {response.status_code == 204}")
