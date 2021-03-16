from requests import get, post

# Получение всех работ
print(get('http://127.0.0.1:8080/api/jobs').json())
# Корректное получение одной работы
print(get('http://127.0.0.1:8080/api/jobs/2').json())
# Ошибочный запрос на получение одной работы — строка
print(get('http://127.0.0.1:8080/api/jobs/r').json())
# Ошибочный запрос на получение одной работы — неверный id
print(get('http://127.0.0.1:8080/api/jobs/233').json())
