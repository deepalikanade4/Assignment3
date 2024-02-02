import requests
import json

URL1='http://127.0.0.1:8000/userdata/'

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL1,data=json_data)
    data=r.json()
    print(data)

get_data(7)

URL2='http://127.0.0.1:8000/createuser/'
def put_data():
    data1={
        'id':3,
        "UserID":1003,
        "Name": 'ABC',
        "EmailID":'ABC@gmail.com',
        "Designation":'Developer'
    }
   
    json_data=json.dumps(data1)
    r=requests.post(url=URL2,data=json_data)
    data=r.json()
    print(data)


put_data()

URL3='http://127.0.0.1:8000/updateuser/'
def update_data():

    data1={
        'id':8,
        "UserID":1012,
        "Name": 'python',
        "EmailID":'python@gmail.com',
        "Destignation":'Python Developer'
    }
    json_data=json.dumps(data1)
    r=requests.put(url=URL3,data=json_data)
    data=r.json()
    print(data)

update_data()

URL4='http://127.0.0.1:8000/deleteuser/'

def deletedata():
    data={'id':22}
    json_data=json.dumps(data)
    r=requests.delete(url=URL4,data=json_data)
    print(r.json())

deletedata()