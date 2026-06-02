import requests

response = requests.get("http://localhost:8000/greet/Aaron")

print("Status Code:", response.status_code)
print("Data:", response.json())