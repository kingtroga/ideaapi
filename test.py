import requests

url = "http://127.0.0.1:8000/api/users/"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk2NTEzMDQyLCJpYXQiOjE2OTY1MTI3NDIsImp0aSI6IjU0NzQ1ODAwYjc3NTRiMTM5NjQ5ODljY2FkMWFkZmIxIiwidXNlcl9pZCI6MTkwMTAzMDEwNDN9.TzD6c6VLkUCg2V6cQkEReBVYo9p-aO9wimAimrlS3_g"
}

response = requests.get(url, headers=headers)
print("123".encode('utf-8'))
print(response.text)
