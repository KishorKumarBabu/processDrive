data={}
def create(key,value):
    if key in data:
        print("key alredy exist")
    else:
        data[key]=value
        print("student name created successfully")
def read(key):
    if key in data:
        print(data[key])
    else:
        print(key," is not exist")
def update(key):
    print(data)
    if key in data:
        del data[key]
        key=input("enter the name to update:")
        if key in data:
                print(key,"is not exist")
            
        else:
            value=int(input("enter the reg no to update:"))
            data[key]=value
            print("The reg no is update successfully")
    print(data)
def delete(key):
    if key in data:
        del data[key]
        print(key,"deleted successfully")
    else:
        print(key," is not exist")
    print(data)
while True:
    option='''
        1.create
        2.read
        3.update
        4.delete
        5.exit
    '''
    print(option)
    n=int(input("enter your choice:"))
    if n==1:
        print("selected create")
        key=input("enter the name of the student:")
        value=int(input("enter the reg no of the student:"))
        print("Entered name is ",key)
        print("Entered reg is",value)
        create(key,value)
    elif n==2:
        print("selected read")
        key=input("enter the name to know the reg no:")
        read(key)
    elif n==3:
        print("selected update")
        key=input("enter the name to update :")
         
        update(key)
    elif n==4:
        print("selected delete:")
        key=input("enter the name to delete the date:")
        delete(key)
    elif n==5:
        print("process exited -----")
        break
    else:
        print("enter valid input -----")
        
        
input()
        
    
    