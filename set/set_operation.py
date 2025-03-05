set1={12,23,45,97,'kishor'}
set2={97,45,99,48,'hari'}
print("set1:",set1)
print("set2:",set2)

#union operation
print("untion:",set1.union(set2))

#inersection operation
print("insertion:",set1 & set2)

#difference operation
print("difference:",set1 - set2)

#symmetric_difference operation
print("symmetric_difference:",set1 ^ set2)

#issubset operation
print("issubset:",set1 <= set2)

#issuperset operation
print("issuperset:",set1 >= set2)

#isdisjoint operation
print("isdisjoin:",set1.isdisjoint(set2))

#inersection_update operation
set1={12,23,45,97,'kishor'}
set2={97,45,99,48,'hari'}
set1.intersection_update(set2)
print("inersection_update:",set1)

#difference_update operation
set1={12,23,45,97,'kishor'}
set2={97,45,99,48,'hari'}
set1.difference_update(set2)
print("difference_update:",set1)

#symmetric_difference_update operation
set1={12,23,45,97,'kishor'}
set2={97,45,99,48,'hari'}
set1.symmetric_difference_update(set2)
print("symmetric_difference_update:",set1)

#update operation
set1={12,23,45,97,'kishor'}
set2={97,45,99,48,'hari'}
set1.update(set2)
print(set1)
