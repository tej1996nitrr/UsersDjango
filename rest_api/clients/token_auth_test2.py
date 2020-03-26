import requests
from django.urls import reverse


def client():
    data = {"username": "tester3",
            "password1": "nerd@123",
            "password2": "nerd@123",
            "email":"testerpy@gmail.com",
            }
    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)
    print("Status_code", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()