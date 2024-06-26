import requests
from pymongo import MongoClient

resp=requests.get('https://jsonplaceholder.typicode.com/users')
user_list=resp.json()

try:
    client=MongoClient('mongodb://localhost:27017/')
    print("MongoDB connection successfully")
    db=client['10am']
    col=db['users']
    col.insert_many(user_list)
    print("Data Inserted Successfully")
except:
    Print("Read the err and rectify with patience")
finally:
    col=None
    db=None
    client=None

