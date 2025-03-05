tup=(20,30,50,50,80,80,3,100,468)
print(tup)

#accessing tuple item
print(tup[0])
print(tup[1])
print(tup[-1])

#sum function
x=sum(tup)
print("sum:",x)

#max function
x=max(tup)
print("max:",x)

#min function
x=min(tup)
print("min:",x)

#count function
x=tup.count(80)
print("count of 80:",x)

#index function
x=tup.index(80)
print("index of 80:",x)

#len function
x=len(tup)
print("length of tuple:",x)

#sorted function
x=sorted(tup)
print(x)

#converting a list into tuple
y=[12,34,56,67,"kishor","hari","archana","jeff"]
print(type(y),y)
x=tuple(y)
print(type(x),x)

input()


