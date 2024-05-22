import pymongo
from pymongo import MongoClient

#print(dir(pymongo))

client= MongoClient("mongodb://localhost:27017")

print("connection successfull")
db=client['9am']

user_collection=db['users']
user_collection.insert_one({'101':101,'name':"Dhinesh",'lastname':"M"})



