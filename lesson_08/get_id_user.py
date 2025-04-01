import requests


url = "https://yougile.com/api-v2/users"

headers = {
    "Authorization": "Bearer WP2OKqffGsqhX5yxsxS0r3XtrrDGzmDClwyvWOxJ0fIwRXJeJVoGe6ULCClXkkWl",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

users_data = response.json()
print("Инфо о сотрудниках: ", users_data)

users = users_data.get('content', [])

print("Список сотрудников: ")
for user in users:
    print(f"ID: {user['id']}, Имя: {user.get('realName')}")