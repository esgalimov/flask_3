from requests import get, post, delete


# все работы корректно
print(get('http://127.0.0.1:8080/api/v2/jobs').json())

# одна работа get корректно
print(get('http://127.0.0.1:8080/api/v2/jobs/1').json())

# одна работа get некорректно
print(get('http://127.0.0.1:8080/api/v2/jobs/999').json())

# delete корректно
print(delete('http://127.0.0.1:8080/api/v2/jobs/2').json())

# delete некорректно
print(delete('http://127.0.0.1:8080/api/v2/jobs/888').json())

# post корректно
print(post('http://127.0.0.1:8080/api/v2/jobs',
           json={'id': 30,
                 'team_leader': 1,
                 'job': 'Test api',
                 'work_size': 1,
                 'collaborators': '2, 3',
                 'start_date': None,
                 'end_date': None,
                 'is_finished': True}).json())

# post некорректно
print(post('http://127.0.0.1:8080/api/v2/jobs',
           json={'id': 30,
                 'team_leader': 1,
                 'job': 'Test api',
                 'work_size': 1,
                 'collaborators': '2, 3',
                 'start_date': None,
                 'end_date': None,
                 'is_finished': True}).json())

# все пользователи get корректно
print(get('http://127.0.0.1:8080/api/v2/jobs').json())
