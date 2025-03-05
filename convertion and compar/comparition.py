#list operation
lst=[23,54,76,87,9]
print(lst)
print(lst[3])
print(lst[-1])

#method
lst.append(35)
lst.extend([34,56,12])
lst.remove(87)
lst.pop(3)
lst.insert(4,24)
print(lst)
lst.reverse()
print(lst)
#____________________________________

#tuple
tup=(23,46,78,16,576)
print(tup)
print(tup[3])
print(tup[-1])

#method
print(tup.count(78))
print(tup.index(576))

#________________________________________

#set
set1={23,46,78,16,576}
print(set1)

#method
set1.add(60)
set1.pop()
set1.remove(46)
set1.discard(23)
print(set1)
set1.clear()
print(set1)

#______________________________________

#dict
dic={"kishor":18,"archana":19,"jeff":21,"hari":19}
print(dic)
print(dic["kishor"])

#method
dic["hari"]=18
dic["kishor"]=18
dic.pop("jeff")
dic.popitem()
print(dic)
dic.clear()
print(dic)
del dic
print(dict)
