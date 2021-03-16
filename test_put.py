from requests import get, put

# Получение всех работ
print(get('http://127.0.0.1:8080/api/jobs').json())

# корректный запрос
print(put('http://127.0.0.1:8080/api/jobs/20',
           json={'id': 25,
                 'job': 'Test 2',
                 'team_leader': 3,
                 'work_size': 5,
                 'collaborators': '2, 3, 7',
                 'is_finished': True}).json())

# существующий id (работа с id = 1 уже есть)
print(put('http://127.0.0.1:8080/api/jobs/25',
           json={'id': 1,
                 'job': 'Test',
                 'team_leader': 1,
                 'work_size': 1,
                 'collaborators': '2, 3',
                 'is_finished': False}).json())


# работы с id = 888 нет
print(put('http://127.0.0.1:8080/api/jobs/888',
           json={'id': 1,
                 'job': 'Test',
                 'team_leader': 1,
                 'work_size': 1,
                 'collaborators': '2, 3',
                 'is_finished': False}).json())


# пустой
print(put('http://127.0.0.1:8080/api/jobs/1',
           json={}).json())


# Получение всех работ
print(get('http://127.0.0.1:8080/api/jobs').json())
