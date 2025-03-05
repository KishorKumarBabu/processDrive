from pymongo import MongoClient

# Replace 'localhost' and '27017' with your MongoDB server address and port
client = MongoClient('localhost', 27017)

# Create a database named 'mydatabase'
db = client['mydatabase']

# Verify that the database is created by listing the databases
print(client.list_database_names())
