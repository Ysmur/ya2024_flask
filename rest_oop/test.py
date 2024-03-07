from pprint import pprint
from requests import get, post, delete

#pprint(get('http://localhost:5000/api/v2/users/2').json())
#pprint(get('http://localhost:5000/api/v2/users/20').json())
#pprint(get('http://localhost:5000/api/v2/users').json())
# pprint(post('http://localhost:5000/api/v2/users',
#            json={'surname': 'Markiz',
#                  'name': 'Tom',
#                  'age': 23,
#                  'position': 'doctor',
#                  'speciality': 'terapevt',
#                  'address': 'module_1',
#                  'email': 'ya@ya.ru',
#                  'hashed_password': '123'}).json())

# pprint(post('http://localhost:5000/api/v2/users',
#             json={'surname': 'Markiz',
#                   'name': 'Tom'}).json())

print(delete('http://localhost:5000/api/v2/users/7').json())
print(delete('http://localhost:5000/api/v2/users/70').json())

pprint(get('http://localhost:5000/api/v2/users').json())
