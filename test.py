from requests import get, post

# Получение всех работ
print(get('http://127.0.0.1:8080/api/jobs').json())
# Корректное получение одной работы
print(get('http://127.0.0.1:8080/api/jobs/2').json())
# Ошибочный запрос на получение одной работы — строка
print(get('http://127.0.0.1:8080/api/jobs/r').json())
# Ошибочный запрос на получение одной работы — неверный id
print(get('http://127.0.0.1:8080/api/jobs/233').json())

print(post('http://127.0.0.1:8080/api/jobs',
           json={'job': 'Test',
                 'team_leader': 1,
                 'work_size': 1,
                 'collaborators': '2, 3',
                 'is_finished': False}).json())

