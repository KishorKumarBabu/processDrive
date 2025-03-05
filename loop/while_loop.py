n=int(input("enter the no of row:"))
row=0
while row<n:# this condition for ror
    space=n-row-1
    while space>0:# this condition for space
        print(end=" ")
        space=space-1
    star=row+1
    while star>0:# this condition for star
        print("*",end=" ")
        star=star-1
    row=row+1
    print()
    
input()
    