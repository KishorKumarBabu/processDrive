lst=[1,34,6,80,60,90]
print("length of list is ",len(lst))

print('access list item')
print(lst[0])

print("change list item")
lst[1]=30
print(lst)

print("adding element using append function")
lst.append(100)
print(lst)

print("sort function")
lst.sort()
print(lst)

print("adding element using extend function")
lst1=[110,120,130,"apple"]
lst.extend(lst1)
print(lst)

print("adding element using insert function")
lst.insert(2,20)
print(lst)

print("reverse function")
lst.reverse()
print(lst)

print("copy function")
newlst=lst.copy()
print(newlst)

print("count function")
print(lst.count(60))

print("index function")
print(lst.index(110))

print("remove function")
lst.remove(6)
print(lst)

print("pop funtion")
print(lst.pop(6))
print(lst)

print("del function")
del lst[9]
print(lst)

print("clear function")
lst.clear()
print(lst)
input()






