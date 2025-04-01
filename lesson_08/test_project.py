import requests


base_url = "https://yougile.com/api-v2/"
user_token = "8oRL6YBkQpg1f3XSwedu9i5RSLIuRHiu2bKGz9pC+KsT50RNeyHDlmlo78dDs7Uc"

headers = {
    "Authorization": f"Bearer {user_token}",
    "Content-Type": "application/json"
}


def create_project(title):
    data = {"title": title}
    response = requests.post(base_url + 'projects', json=data, headers=headers)
    assert response.status_code == 201
    print("Проект создан")
    project_id = response.json().get('id')
    return project_id


# создать проект
def test_create_project():
    data = {"title": "Проект ДЗ"}
    response = requests.post(base_url+'projects', json=data, headers=headers)
    assert response.status_code == 201
    print("Проект создан")


# получить список проектов
def test_get_projects():
    response = requests.get(base_url+'projects', headers=headers)
    assert response.status_code == 200
    print("Проекты получены")


# получить проект по ID
def test_get_project_by_id():
    test_project_id = create_project("Проект ДЗ")
    response = requests.get(base_url + f'projects/{test_project_id}', headers=headers)
    assert response.status_code == 200
    print("Проект по ID получен")


# изменить проект
def test_change_project():
    test_project_id = create_project("Проект PUT")
    data = {"title": "Проект с изменениями"}
    response = requests.put(base_url + f'projects/{test_project_id}', json=data, headers=headers)
    assert response.status_code == 200
    print("Проект изменён")


# создать проект без названия
def test_create_project_without_title():
    data = {"description": "Проект без названия"}
    response = requests.post(base_url+'projects', json=data, headers=headers)
    assert response.status_code == 400


# получить проект по неверному ID
def test_get_project_by_invalid_id():
    response = requests.get(base_url + 'projects/4f6f0391-0f94-4d30-9b0e-99430a36d4fb', headers=headers)
    assert response.status_code == 404


# изменить проект с неверными данными
def test_change__invalid_project():
    data = {"title": "Проект с изменениями"}
    response = requests.put(base_url + f'projects/4f6f0391-0f94-4d30-9b0e-99430a36d4fb', json=data, headers=headers)
    assert response.status_code == 404