import requests
import json
from pprint import pprint
"""
r = requests.get('http://127.0.0.1:8000/api/category/')

print(r.status_code)
print(r.headers['content-type'])
print('r.text : ', r.text)

json_data = json.loads(r.text)
print('json_data : ', json_data[0])
print('json_data : ', json_data[1])
print('json_data : ', json_data[2])
print('json_data : ', json_data[3])

"""

# r = requests.get('http://127.0.0.1:8000/api/shop/')
#
# json_data = json.loads(r.text)
# for j in json_data:
#     print(j)

# r = requests.get('http://127.0.0.1:8000/api/shop/2/')
#
# print(r.text)
#
# r = requests.get('http://127.0.0.1:8000/api/shopitems/')
#
# loads_data = json.loads(r.text)
# for l in loads_data:
#     pprint(l)


# r = requests.get('http://127.0.0.1:8000/api/category/')
#
# print(r.status_code)
# print(r.text)
#
# data = json.loads(r.text)
#
# pprint(data)
#
# data = {
#     'client':1,
#     'total':450000,
#     'status':1
# }
#
# r = requests.post('http://127.0.0.1:8000/api/shop/', data)
# print(r.text)
#
# data = {
#     "total":350000,
#     "status":2
# }
#
# r = requests.put('http://127.0.0.1:8000/api/shop/4/', data)
# print(r.text)

r = requests.delete('http://127.0.0.1:8000/api/shop/3/')
print(r.text)