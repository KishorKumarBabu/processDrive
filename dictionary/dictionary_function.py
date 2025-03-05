dicte={"name":"kishor","age":19,"ph no":8907357726}

print('accessing dictionary item')
print(dicte["name"])

print("printing keys")
x=dicte.keys()

print("printing the values")
print(dicte.values())

print("changing dictionary item")
dicte["age"]=18
print(dicte)

print("add items")
dicte["regno"]=59
print(dicte)

print("update function")
dicte.update({"regno":"059"})
print(dicte)

print("pop function")
print(dicte.pop("ph no"))
print(dicte)

print("popitem function")
dicte.popitem()
print(dicte)

print("del function")
del dicte['name']
print(dicte)

print('clear function')
dicte.clear
print(dicte)


input()






