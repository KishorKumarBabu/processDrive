from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client["mydatabase"]
collection=db["data"]
def create_doc(post):
    if collection.find_one({"_id":post["_id"]}):
        print("It is alredy in database")
    else:
        collection.insert_one(post)
        print("The document is created sucessfully")
def read_doc(name):
    result=collection.find_one({"name":name})
    print(result)
def read_all_doc():
    result=collection.find({})
    for x in result:
        print(x)
def update(id):
    if collection.find_one({"_id":id}):
        job=input("Enter the job:")
        collection.update_many({"_id":id},{"$set":{"job":job}})
        result=collection.find_one({"_id":id})
        print(result)
        print('Updated document sucessfully.')
        
    else:
        print("user is not found.")
def delete(name):
    if collection.find_one({"name":name}):
        collection.delete_one({"name":name})
        print("Deleted document successfully.")
    else:
        print("The document is not found.")
    
while True:
    option='''
    1.Create Document
    2.Read Specific Document
    3.Read All Document
    4.Update Document
    5.Delete Document
    6.Exit
    '''
    print(option)
    n=int(input("Enter the choice:"))
    if n == 1:
        post={"_id":int(input("Enter id to create: ")),
              "name":input("Enter the name:"),"job":input("Enter the job:")}
        create_doc(post)
    elif n==2:
        name=input("Enter a name:")
        read_doc(name)
    elif n==3:
        read_all_doc()
    elif n==4:
        id=int(input("enter the id:"))
        update(id)
    elif n==5:
        name=input("enter the name to delete:")
        delete(name)
    elif n==6:
        print("Exit.............")
        break
input()
    