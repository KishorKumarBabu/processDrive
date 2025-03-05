from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client["mydatabase"]
collection=db["data"]
post1={"_id":1,"name":"hari","job":"devops"}
post2={"_id":2,"name":"archana","job":"python"}

collection.insert_many([post1,post2])
