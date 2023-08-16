import requests

api_url = "http://127.0.0.1:8000/api/avatar/"  # Update with your actual API endpoint
token = "aef8b8ce3fb45cddc7f6ae8825776da3767d1d7d"  # Replace with your token

file_path = r"C:\Users\ADMIN\Downloads\teddy.png"

headers = {
    "Authorization": f"Token {token}",
}

data = {
    "avatar": ("filename.jpg", open(file_path, "rb"), "image/jpeg"),
}

response = requests.post(api_url, headers=headers, files=data)

print(response.status_code)
print(response.text)
