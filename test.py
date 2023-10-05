import requests

url = "http://127.0.0.1:8000/api/users/"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk2NTA3NDcxLCJpYXQiOjE2OTY1MDcxNzEsImp0aSI6IjcwNWIzNjIxYjViYjRhMGRiYzlhZjQzYWEyMzE5YTc5IiwidXNlcl9pZCI6MTkwMTAzMDEwNDN9.izh8X3qm8VaV5W-mS09zuz2PacxerTwjD4NOP5U2XsE"
}

response = requests.get(url, headers=headers)

print(response.text)
