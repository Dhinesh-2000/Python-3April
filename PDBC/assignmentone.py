import requests
from pymongo import MongoClient
import json

resp=requests.get('https://jsonplaceholder.typicode.com/users')
user_list=resp.json()

client=MongoClient('mongodb://localhost:27017/')
db=client['9am']
user_collection=db['users']

user_collection.insert_many(user_list)

print("Inserted successfully")



