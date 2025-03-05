from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client["mydatabase"]
collection=db["data"]
post={"_id":0,"name":"kishor","job":"software"}
collection.insert_one(post)
