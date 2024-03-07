from pprint import pprint
from requests import get, post

#pprint(get('http://localhost:5000/api/v2/users/2').json())
#pprint(get('http://localhost:5000/api/v2/users/20').json())
##????print(get('http://localhost:5000/api/v2/users/q').json())
pprint(get('http://localhost:5000/api/v2/users').json())