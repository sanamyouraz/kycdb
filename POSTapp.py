import requests
import json

url = "http://localhost:8000/users/"

data = {
    "id": 1,
    "username": "neha kumar chaudhary",
    "email": "nehakumar123@gmail.com",
    "phone_number": "9845841246",
    "password": "rddd",
    "confirm_password": "rddd"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.json())
