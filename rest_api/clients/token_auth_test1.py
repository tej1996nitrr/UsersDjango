import requests
from django.urls import reverse


def client():
    token_h="Token b237295748a387ec7e534acc9e6491bab807e8d3"
    credentials = {"username": "admin", "password": "admin"}
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)
    header={"Authorization":token_h}
    response = requests.get("http://127.0.0.1:8000/profiles/",headers=header)

    print("Status_code", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
