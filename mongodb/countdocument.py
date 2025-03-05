from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client["mydatabase"]
collection=db["data"]
a=collection.count_documents({})
print(a)
