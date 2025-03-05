from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client["mydatabase"]
collection=db["data"]
result=collection.find({"name":'hari'})
a=collection.find({})
for x in result:
    print(x)
for x in a:
    print(x)
