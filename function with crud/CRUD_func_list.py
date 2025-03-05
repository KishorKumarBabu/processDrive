data=[]

def create(name, reg):
    for item in data:
        if item[0]==name:
            print("Name already exists")
    data.append((name, reg))
    print("Student record created successfully")

def read(name):
    for item in data:
        if item[0]==name:
            print(item[1])
            break
    else:
            print(name, "is not exist")

def update(name):
    print(data)
    for i, item in enumerate(data):# this line is used to get the data as will as increasing the index value
        if item[0]==name:
            name=input("enter a name to update")
            reg=int(input("enter the reg no to update: "))
            data[i]=(name,reg)
            print("updated successfully")
            break
    else:
        print(name, "is not exist")
    print(data)

def delete(item):
    i=0
    for item in data:
        if item[0]==name:
            del data[i]
            print(name, "deleted successfully")
            i+=1
            break
    else:
        print(name, "is not exist")
    print(data)

while True:
    option='''
        1. create
        2. read
        3. update
        4. delete
        5. exit
    '''
    print(option.center(200))
    n=int(input("enter your choice: "))
    
    if n==1:
        print("selected create")
        name=input("enter the name of the student: ")
        reg=int(input("enter the reg no of the student: "))
        create(name, reg)
        
    elif n==2:
        print("selected read")
        name=input("enter the name to know the reg no: ")
        read(name)
        
    elif n==3:
        print("selected update")
       
        update(name)
        
    elif n==4:
        print("selected delete")
        name=input("enter the name to delete the data: ")
        delete(name)
        
    elif n==5:
        print("process exited ---------")
        break
        
    else:
        print("enter valid input ---------")
input()