from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client["mydatabase"]
collection=db["data"]
result=collection.find_one({"_id":2})
print(result)