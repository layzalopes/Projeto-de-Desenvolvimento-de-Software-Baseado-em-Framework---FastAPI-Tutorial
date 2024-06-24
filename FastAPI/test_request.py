import requests

url = "http://localhost:8000/users/"
payload = {
    "email": "user@example.com",
    "password": "password123"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.json())
