from requests import get, post

# Получение всех работ
print(get('http://127.0.0.1:8080/api/jobs').json())

# корректный запрос
print(post('http://127.0.0.1:8080/api/jobs',
           json={'id': 20,
                 'job': 'Test',
                 'team_leader': 1,
                 'work_size': 1,
                 'collaborators': '2, 3',
                 'is_finished': False}).json())

# не содержит все требуемые поля
print(post('http://127.0.0.1:8080/api/jobs',
           json={'id': 20,
                 'team_leader': 1,
                 'work_size': 1,
                 'collaborators': '2, 3',
                 'is_finished': False}).json())

# пустой
print(post('http://127.0.0.1:8080/api/jobs',
           json={}).json())

# существующий id
print(post('http://127.0.0.1:8080/api/jobs',
           json={'id': 20,
                 'job': 'Test',
                 'team_leader': 1,
                 'work_size': 1,
                 'collaborators': '2, 3',
                 'is_finished': False}).json())

# Получение всех работ
print(get('http://127.0.0.1:8080/api/jobs').json())


