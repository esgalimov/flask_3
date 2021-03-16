from requests import get, delete

# Получение всех работ
print(get('http://127.0.0.1:8080/api/jobs').json())

# работы с id = 999 нет в базе
print(delete('http://127.0.0.1:8080/api/jobs/999').json())

# строка в id
print(delete('http://127.0.0.1:8080/api/jobs/y').json())

# корректный запрос
print(delete('http://127.0.0.1:8080/api/jobs/25').json())

# Получение всех работ
print(get('http://127.0.0.1:8080/api/jobs').json())