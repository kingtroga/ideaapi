import requests

def login(username, password):
    login_url = "http://127.0.0.1:8000/dj-rest-auth/login/"
    data = {
        "username": username,
        "password": password,
    }

    response = requests.post(login_url, data=data)

    if response.status_code == 200:
        print("Login successful!")
        print("Response data:", response.json())
    else:
        print("Login failed!")
        print("Error message:", response.json())

if __name__ == "__main__":
    # Replace the credentials with the actual username and password
    username = "19010301043"
    password = "janet2003"

    login(username, password)
