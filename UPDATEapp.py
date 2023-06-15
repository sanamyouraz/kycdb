import requests
import json

url = "http://localhost:8000/users/"

data = {
    "id": 2,
    "username": "neha kumar chaudhary",
    "email": "nehakumar123@gmail.com",
    "phone_number": "9845841246",
    "password": "rddd",
    "confirm_password": "rddd"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.put(url + str(data['id']), data=json.dumps(data), headers=headers)

try:
    response_json = response.json()
    print(response_json)
except json.decoder.JSONDecodeError:
    print("Response is not in JSON format:")
    print(response.text)
