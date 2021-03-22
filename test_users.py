from requests import get, post, delete


# все пользователи get корректно
print(get('http://127.0.0.1:8080/api/v2/users').json())

# один пользователь get корректно
print(get('http://127.0.0.1:8080/api/v2/users/1').json())

# delete корректно
print(delete('http://127.0.0.1:8080/api/v2/users/4').json())

# delete некорректно
print(delete('http://127.0.0.1:8080/api/v2/users/888').json())

# post корректно
print(post('http://127.0.0.1:8080/api/v2/users',
           json={'id': 9,
                 'surname': 'Watson',
                 'name': 'John',
                 'age': 30,
                 'position': 'Doctor',
                 'speciality': 'Space Doctor',
                 'address': 'module_2',
                 'email': 'watson@mars.com'}).json())

# post некорректно
print(post('http://127.0.0.1:8080/api/v2/users',
           json={'id': 9,
                 'surname': 'Toby',
                 'name': 'Tony',
                 'age': 37,
                 'position': 'Doctor',
                 'speciality': 'Space Doctor',
                 'address': 'module_2',
                 'email': 'Toby@mars.com'}).json())

# все пользователи get корректно
print(get('http://127.0.0.1:8080/api/v2/users').json())