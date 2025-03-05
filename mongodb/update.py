from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client["mydatabase"]
collection=db["data"]
collection.update_many({"_id":2},{"$set":{"job":"frontend"}})
