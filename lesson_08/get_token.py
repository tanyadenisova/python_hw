import requests


url = "https://yougile.com/api-v2/auth/keys"

creds = {
    "login": "",
    "password": "",
    "companyId": "895bd234-81aa-47a2-83aa-f0853005b0fd"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.post(url, json=creds, headers=headers)

token = response.json().get("key")
print(f"Токен: {token}")