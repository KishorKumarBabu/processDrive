# url:https://reqres.in/api/users
import requests,json

def get(url):
    a=requests.get(url)
    return json.dumps(a.json(),indent=4)


def post(url,data):
    headers = {'Content-Type': 'application/json'}
    a=requests.post(url,headers=headers,data=json.dumps(data))
    if a.status_code == 201:
        print("Created successfully.")
    else:
        print("unable to create status code is",a.status_code)
    return json.dumps(a.json(),indent=4)


def put(url,data):
    headers = {'Content-Type': 'application/json'}
    a=requests.put(url,headers=headers,data=json.dumps(data))
    if a.status_code == 200:
        print("Updated successfully.")
    else:
        print("unable to update status code is",a.status_code)
    return json.dumps(a.json(),indent=4)


def patch(url,data):
    headers = {'Content-Type': 'application/json'}
    a=requests.patch(url,headers=headers,data=json.dumps(data))
    if a.status_code == 200:
        print("Updated successfully.")
    else:
        print("unable to update status code is",a.status_code)
    return json.dumps(a.json(),indent=4)


def delete(url):
    a=requests.delete(url)
    if a.status_code == 204:
        print("Delete successfully.")
    else:
        print("unable to delete the user status code is",a.status_code)
while True:
    option='''
    1.Get
    2.Post
    3.Put
    4.Patch
    5.Delete
    6.Exit'''
    print(option)
    n=int(input("Enter your choice:"))
    if n==1:
        a=input("Enter the URL:")
        print(get(a))
        
        
    elif n==2:
        a=input("Enter the URL:")
        data={
            "name":input("Enter the name:"),
            "job":input("Enter the job:"),
            }
        print(post(a,data))
        
        
    elif n==3:
        a=input("Enter the URL:")
        data={
            "name":input("Enter the name:"),
            "job":input("Enter the job:"),
            }
        print(put(a,data))
        
        
    elif n==4:
        a=input("Enter the URL:")
        data={
            "name":input("Enter the name:"),
            "job":input("Enter the job:"),
            }
        print(patch(a,data))
        
        
    elif n==5:
        a=input("Enter the URL:")
        delete(a)
        
        
    elif n==6:
        print("The Process End ---------------")
        break
    
    
    else:
        print("Enter The Valid Choice")
        
        
input()