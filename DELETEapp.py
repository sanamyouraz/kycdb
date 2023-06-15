import requests

url = "http://localhost:8000/users/5"  # Assuming the endpoint for deleting a user is "/users/{id}"

headers = {
    "Content-Type": "application/json"
}

response = requests.delete(url, headers=headers)

if response.status_code == 204:  # Successful deletion (No Content)
    print("User deleted successfully.")
elif response.status_code == 404:  # User not found
    print("User not found.")
else:
    print("An error occurred while deleting the user.")
